FROM rasa/rasa:latest-full

COPY . ../bot 

WORKDIR /bot 

RUN pip3 install -r requirements.txt

EXPOSE 5055

CMD ['hello.py', 'python']

