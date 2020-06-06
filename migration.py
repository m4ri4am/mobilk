import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db
#.get zeyada
app.config.from_object(os.environ['APP_SETTINGS'])
# /home/magda/Desktop/postgre-flask-project/env

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run()