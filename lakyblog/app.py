from flask import Flask, request, redirect, url_for
import flask.ext.login as flask_login
from lakyblog.model import db_session, User
from lakyblog.setting import setting, parse_config_file
import os, logging

class LakyBlogApp(Flask):

    def __init__(self, import_name, static_path=None, static_url_path=None,
                static_folder='static', template_folder='templates',
                instance_path=None, instance_relative_config=False):

        Flask.__init__(self, import_name, static_path, static_url_path,
                    static_folder, template_folder,
                    instance_path, instance_relative_config)

        self.config.update({'SECRET_KEY': os.urandom(24),
                            'LOGGER_NAME': 'lakyblog'})

        logging.config.dictConfig(setting['logging'])
        self._logger = logging.getLogger('lakyblog')


app = LakyBlogApp(__name__)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def user_loader(id):
    return User.query.filter(User.id == id).first()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    import logging
    logging.getLogger('lakyblog').debug('12312312')
    app.logger.debug('123')
    1 / 0
    if request.method == 'POST':
        user = User.query.\
            filter(User.username == request.form['username']).\
            filter(User.password == request.form['password']).\
            first()
        if user is None:
            return '`username` or `password` is wrong.'
        else:
            flask_login.login_user(user)
            return redirect(url_for('home'))
    else:
        return 'TODO'
