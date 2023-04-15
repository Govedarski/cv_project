import random
from time import sleep

from flask import current_app

from config import create_app
from db import db

app = create_app()


@app.after_request
def return_response(response):
    db.session.commit()
    if current_app.debug and not current_app.testing:
        sleep(random.randint(0, 1))
    return response


if __name__ == '__main__':
    app.run()
