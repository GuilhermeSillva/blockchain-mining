import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main import create_app, data_base
from app import blueprint

# models
from app.main.model.block import block_model

app = create_app(os.getenv('APP_ENV'))
app.register_blueprint(blueprint)
manager = Manager(app)

migrate = Migrate(app, data_base)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()
