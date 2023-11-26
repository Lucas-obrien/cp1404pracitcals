from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def convert_celsius_to_fahrenheit(celsius):
    """Converts celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


@app.route('/f')
@app.route('/f/<number>')
def fahrenheit(number=""):
    return f"{convert_celsius_to_fahrenheit(float(number))}"


if __name__ == '__main__':
    app.run()
