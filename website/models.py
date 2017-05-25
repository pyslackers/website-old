from flask_login import UserMixin

from website.external import db


roles_users = db.Table('roles_users',
                       db.Column('role_id', db.ForeignKey('role.id',
                                                          ondelete='CASCADE'),
                                 nullable=False),
                       db.Column('user_id', db.ForeignKey('user.id',
                                                          ondelete='CASCADE'),
                                 nullable=False),
                       db.UniqueConstraint('role_id', 'user_id',
                                           name='ux_role_user'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    slack_user_id = db.Column(db.String, nullable=False)
    slack_team_id = db.Column(db.String, nullable=False)

    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    __table_args__ = (
        db.UniqueConstraint(slack_user_id, slack_team_id,
                            name='ux_slack_user_slack_team'),
    )


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
