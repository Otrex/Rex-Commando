import pyautogui
from flask import request, jsonify, Blueprint
from models.User import User, db

app = Blueprint('home', __name__, url_prefix="/home")