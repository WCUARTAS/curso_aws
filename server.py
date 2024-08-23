from flask import Flask, render_template
from database.db import get_db

app = Flask(__name__)

from routes.routes import *


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "80"
    app.run(host,port)