# Flask for Hello World 

from Flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
    
