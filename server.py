from app import application
from app.routes.routes import initialize_routes

if __name__ == '__main__':
    application.run(debug=True)

    initialize_routes(application)
