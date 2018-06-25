from flask import Flask
from flask_script import Manager,Server
from flask_migrate import MigrateCommand

from user import create_app

app = create_app()
manager = Manager(app=app)

manager.add_command('start',Server(host='127.0.0.1',port=9000))
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
   app.run()
