from aiohttp import BodyPartReader

from flask import Flask,render_template,redirect,url_for
from pyfirmata import Arduino

app = Flask(__name__)
global board,motor
board = Arduino("COM4")
motor = board.get_pin('d:10:s')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aumentar')
def set_aumentar():
    board.digital[9].write(1)
    return redirect(url_for('/'))


app.run()