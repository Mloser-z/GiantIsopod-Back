from flask import Flask
from flask_cors import CORS

from blueprints.image import bp as image_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.register_blueprint(image_bp)
CORS(app=app, supports_credentials=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
