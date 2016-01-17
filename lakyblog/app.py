from flask import Flask, request, redirect, url_for
import flask.ext.login as flask_login
from lakyblog.model import db_session, User, init_db
from lakyblog.config import config
import os, logging
from logging.config import dictConfig as logging_dict_config

class LakyBlogApp(Flask):

    def __init__(self, import_name):

        Flask.__init__(self, import_name)

        self.__basic_app_config()

        self.__init_logger()

        self.__init_login_manager()

        init_db()

    def __basic_app_config(self):
        self.config.update({'SECRET_KEY': os.urandom(24),
                            'LOGGER_NAME': 'lakyblog'})

    def __init_logger(self):
        logging_dict_config(config['logging'])
        self._logger = logging.getLogger('lakyblog')

    def __init_login_manager(self):
        self.login_manager = flask_login.LoginManager()
        self.login_manager.init_app(self)

app = LakyBlogApp(__name__)


@app.login_manager.user_loader
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
