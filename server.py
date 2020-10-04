from flask import Flask
from routes.routes import initialize_routes


app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
    initialize_routes(app)
