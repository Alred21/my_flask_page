from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    # Load the configuration file
    app.config.from_object('config.Config')
    app.config.from_pyfile('config.py', silent=True)
    
    # Import the routes
    from . import routes
    app.register_blueprint(routes.bp)

    return app
