from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    # Run on a custom port, e.g., 5001
    app.run(host='0.0.0.0', port=5001, debug=True)
