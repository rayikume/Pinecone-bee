import os
from pathlib import Path
from flask import Flask
from flask_socketio import SocketIO
from dotenv import load_dotenv
from .config import DevConfig
from .routes.views import views
from .sockets.events import register_events


socketio = SocketIO(cors_allowed_origins="*")

# Load environment from .env (and fallback to .env.dev) early
load_dotenv()  # loads .env if present
dev_env = Path(__file__).resolve().parents[1] / ".env.dev"
if dev_env.exists():
    load_dotenv(dev_env, override=False)


def create_app(config_object: type = DevConfig) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Blueprints
    app.register_blueprint(views)

    # Sockets
    socketio.init_app(app, cors_allowed_origins="*")
    register_events(socketio)

    return app
