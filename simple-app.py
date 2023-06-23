import os
from flask import Flask
app=Flask(__name__)

@app.route("/")
def main():
    return "welcome"

@app.route('/docker/commands')
def hello():
    return "<h1>Docker Commands</h1><ul><li>docker images</li><li>docker search {image_name}</li><li>docker pull {image_name}</li><li>docker run</li>"

if __name__ == "__main__":
    app.run()
