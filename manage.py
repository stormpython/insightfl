#!/usr/bin/env python
from app import app
from flask.ext.script import Manager, Shell

# The Flask-Script extension provides support for writing external scripts in
# Flask, which includes running a development server. For more info, visit:
# http://flask-script.readthedocs.org/en/latest/.
manager = Manager(app)


def make_shell_context():
    return dict(app=app)

manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
