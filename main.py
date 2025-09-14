from flask import Flask, render_template, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO,  
                    format='%(message)s',  
                    handlers=[
                        logging.FileHandler('webserver_logs.log'),  
                        logging.StreamHandler()
                    ])

@app.route('/')
def home():
    return render_template('index.html')

@app.before_request
def log_request_info():
    ip = request.remote_addr
    method = request.method
    path = request.path

    log_data = f"{ip} {method} {path}"
    app.logger.info(log_data)

if __name__ == '__main__':
    app.logger.propagate = False
    app.run(debug=True, host="0.0.0.0", port=5000)
