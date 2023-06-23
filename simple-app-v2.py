import os
from flask import Flask
app=Flask(__name__)

@app.route("/")
def main():
    return "welcome"

@app.route('/docker/commands')
def commands():
    return "<h1>Docker Commands</h1><ul><li>docker images</li><li>docker search {image_name}</li><li>docker pull {image_name}</li><li>docker run</li>"


@app.route('/docker/directives')
def directives():
    return "<h1>Docker Directives</h1><ul><li>FROM</li><li>RUN</li><li>EXPOSE</li><li>COPY</li><li>ADD</li><li>ENTRYPOINT</li>"

if __name__ == "__main__":
    app.run()
