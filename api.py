
from app import app_
from src.config import PORT
import frases
import prueba
from src.helpers.error_helper import errorHelper, APIError, Error404, checkValidParams
from src.helpers.js_answ import data

app_.run("0.0.0.0", PORT, debug=True)