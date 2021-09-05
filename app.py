from flask import Flask
app = Flask(__name__)


print("hello")

@app.route("/")
def app():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)