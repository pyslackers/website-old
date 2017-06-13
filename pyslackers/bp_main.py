import requests
from flask import (
    Blueprint,
    current_app,
    flash,
    render_template,
)

from .forms import InviteRequestForm


bp_main = Blueprint('main', __name__)


@bp_main.route('/', methods=['GET', 'POST'])
def index():
    form = InviteRequestForm()
    if form.validate_on_submit():
        # TODO: this should be abstracted out to another class
        r = requests.post('https://slack.com/api/users.admin.invite', data={
            'token': current_app.config['SLACK']['api_token'],
            'email': form.email.data,
            'channels': current_app.config['SLACK']['join_channels'],
            'resend': True,
        })
        if r.json()['ok']:
            flash('Invite sent!', category='info')
        else:
            flash('Error trying to send: ' + r.json().get('error'),
                  category='warning')
    return render_template('main/index.html', form=form,
                           # TODO: pull from dynamic source
                           projects=[
                               {
                                   'title': 'SirBot-A-Lot',
                                   'description':
                                   'A pluggable community driven bot,'
                                   ' utilizing asyncio',
                                   'url':
                                   'https://github.com/pyslackers/'
                                   'sir-bot-a-lot', 'image_url':
                                   'https://github.com/pyslackers/'
                                   'sir-bot-a-lot'
                                   '/blob/master/icon/icon-500.png?raw=true',
                               },
                               {
                                   'title': 'PySlackers Website',
                                   'description':
                                   'A community website, used as a way for the'
                                   ' community to teach younger Python '
                                   'developers and bring in new members.',
                                   'url':
                                   'https://github.com/pyslackers/website',
                                   'image_url':
                                   'https://github.com/pyslackers/'
                                   'sir-bot-a-lot'
                                   '/blob/master/icon/icon-500.png?raw=true',
                               },
                               {
                                   'title': 'Community Resources',
                                   'description':
                                   'Resources for Python developers of '
                                   'all skill levels.'
                                   'Curated to not waste people\'s time.',
                                   'url':
                                   'https://github.com/pyslackers/learning-'
                                   'resources',
                                   'image_url':
                                   'https://github.com/pyslackers/'
                                   'sir-bot-a-lot'
                                   '/blob/master/icon/icon-500.png?raw=true',
                               },
                           ])
