from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file

app = Flask(__name__)   

@app.route('/<random_string>')

def return_backward_string(random_string):
    """
    Returns the input string in reverse order.
    """
    return "".join(reversed(random_string)) 
@app.route('/get-mode')

def get_mode():
    """
    Returns the mode of the application.
    """
    mode = os.environ.get('MODE')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # Run the Flask app