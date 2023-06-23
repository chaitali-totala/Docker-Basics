FROM ubuntu
RUN apt-get update && apt-get install -y python3 
RUN apt-get install -y  pip && pip install flask
COPY app.py /opt/app.py
EXPOSE 5000/tcp
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=5000
