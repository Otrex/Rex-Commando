import pyautogui
from flask import request, jsonify, Blueprint
from scripts.CommandExecutor import Executor
from models.User import User, db


app = Blueprint('mouse', __name__, url_prefix="/mouse")

@app.route('/', methods=['POST'])
def name():
  x = request.json['username']
  y = request.json['email']

  add_user(x, y)

  return jsonify({'result': 'success'})

@app.route('/move', methods=['POST'])
def move_mouse():
  x = request.json['x']
  y = request.json['y']
  pyautogui.moveTo(x, y)
  return jsonify({'result': 'success'})

@app.route('/click', methods=['POST'])
def click_mouse():
  button = request.json['button']
  pyautogui.click(button=button)
  return jsonify({'result': 'success'})

@app.route('/run_command', methods=['POST'])
def run_command():
    # Get the command and password from the request data
    data = request.get_json()
    command = data['command']
    password = data['password']

    response = Executor.sudo_executor(command, password).to_json()

    return response

