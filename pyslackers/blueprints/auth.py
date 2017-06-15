from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    session,
    url_for,
)
from flask_login import login_user, logout_user

from pyslackers.external import db, slack_oauth
from pyslackers.models import User


bp_auth = Blueprint('auth', __name__)


@bp_auth.route('/login')
def login():
    return render_template('auth/login.html')


@bp_auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp_auth.route('/login/slack')
def login_slack():
    cb_url = url_for('.login_slack_callback', _external=True)
    return slack_oauth.authorize(callback=cb_url)


@bp_auth.route('/login/slack/callback')
def login_slack_callback():
    resp = slack_oauth.authorized_response()
    if resp is None:
        flash('Error logging in', category='error')
        return redirect(url_for('.login'))
    session['slack_token'] = resp['access_token']

    user = User.query.filter_by(slack_user_id=resp['user']['id'],
                                slack_team_id=resp['team']['id']).first()
    if user is None:
        user = User(name=resp['user']['name'],
                    slack_user_id=resp['user']['id'],
                    slack_team_id=resp['team']['id'])
        db.session.add(user)
        db.session.commit()

    login_user(user)

    flash('You have logged in successfully', category='info')
    return redirect(url_for('main.index'))
