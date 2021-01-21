from app import create_app
from os import environ


application = create_app("development")

if __name__ == '__main__':
    application.run()
