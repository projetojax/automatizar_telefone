from flask import Flask, render_template, jsonify
import subprocess
from src.settings import initialize_logging
import logging

app = Flask(__name__)

@app.route('/')
def index():
    logging.info('web_interface >> public >> index')
    return render_template('index.html')

@app.route('/run_bot', methods=['POST'])
def run_bot():
    logging.info('web_interface >> public >> run_bot')
    subprocess.Popen(['python', 'src/main.py'])
    return 'Bot iniciado com sucesso!'

@app.route('/bot_status')
def bot_status():
    logging.info('web_interface >> public >> bot_status')
    return jsonify({'status': 'Concluído'})

