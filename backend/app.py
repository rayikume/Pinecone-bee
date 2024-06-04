from flask import Flask
from flask_cors import CORS
from views import views
from models import models_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(views, url_prefix="/views")
app.register_blueprint(models_bp, url_prefix="/models")

if __name__ == "__main__":
    app.run(debug=True, port=5000)