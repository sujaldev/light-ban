from flask import Flask
from controller import Controller
from threading import Thread
import json

app = Flask(__name__)


def get_controller():
    with open("config.json") as config_file:
        config = json.load(config_file)
        api_controller = Controller(
            config["username"],
            config["password"],
            config["country_code"],
            config["biz_type"]
        )
    return api_controller


CONTROLLER = get_controller()


@app.route('/enable-light-ban')
def enable_light_ban():
    CONTROLLER.ban_enabled = True
    ban_thread = Thread(target=CONTROLLER.enable_ban(), args=())
    ban_thread.start()
    return {"ban_state": True}


@app.route('/disable-light-ban')
def disable_light_ban():
    CONTROLLER.ban_enabled = False
    return {"ban_state": False}


@app.route("/")
def home():
    with open("ui.html") as html:
        return html.read()


if __name__ == '__main__':
    app.run()
