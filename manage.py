#!/usr/bin/env python3.8
# Copyright (c) 2021 Benjamin Lorenz
#

import os
from app import create_app, mongo
from flask_script import Manager, Shell

flask_config = os.getenv('FLASK_CONFIG') or 'production'
print('Using Flask config: ' + flask_config)
app = create_app(flask_config)
manager = Manager(app)


def make_shell_context():
    return dict(app=app)
manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def bootstrap():
    """Initialize database"""
    pass


@manager.command
def fake():
    """Generate fake data"""
    pass


if __name__ == '__main__':
    manager.run()
