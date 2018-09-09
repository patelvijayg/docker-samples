FROM python:3.7-alpine

# Set the application directory
WORKDIR /app

# Install our requirements.txt
#ADD requirements.txt /app/requirements.txt
#RUN pip install -r requirements.txt

RUN pip install flask 
#RUN pip install pyopenssl


ADD ./app /app

EXPOSE 5000

CMD [ "python", "/app/pythonWebServer.py" ]

#docker build --rm -t pytest1 .
#docker run -it --name=pytest -p 5100:5100  pytest1