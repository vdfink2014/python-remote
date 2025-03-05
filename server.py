import keyboard
from flask import Flask, request, jsonify, send_file
from PIL import ImageGrab
import pyautogui
pyautogui.FAILSAFE = False
def click():
    pyautogui.click()
def move_mouse(x,y):
    pyautogui.moveTo(x,y)
app = Flask(__name__)


@app.route('/screenshot', methods=['POST',"GET"])
def take_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    file = open("screenshot.png", "rb")
    return send_file("screenshot.png", mimetype='image/png')

@app.route("/click", methods=['POST'])
def click_():
    click()
    return "",204

@app.route("/move", methods=['POST'])
def move():
    move_mouse(request.json["x"],request.json["y"])
    return "",204

@app.route("/keys", methods=['POST'])
def keys():
    keys = request.json["keys"]
    for key in keys:
        print(key)
    keyboard.press_and_release(keys)
    return "",204


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)