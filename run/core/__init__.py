#!/usr/bin/env python3

import os
from flask import Flask
from core.controllers.general import controller as general
from core.controllers.bicycle import controller as bicycle


def keymaker(omnibus, filename = 'secret_key'):
    pathname = os.path.join(omnibus.instance_path, filename)
    print('pathname: ', pathname )
    try:
        omnibus.config['SECRET_KEY'] = open(pathname, 'rb').read()
    except IOError:
        parent_directory = os.path.dirname(pathname)
        if not os.path.isdir(parent_directory):
            os.system('mkdir -p {}'.format(parent_directory))
        os.system('head -c 24 /dev/urandom > {}'.format(pathname))
        omnibus.config['SECRET_KEY'] = open(pathname, filename)


omnibus = Flask(__name__)
omnibus.register_blueprint(general)
omnibus.register_blueprint(bicycle)
keymaker(omnibus)

