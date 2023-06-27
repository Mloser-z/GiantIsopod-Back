from flask import Flask
from flask_cors import CORS

from blueprints.bp_image import bp as bp_image

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.register_blueprint(bp_image)
CORS(app=app, supports_credentials=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
