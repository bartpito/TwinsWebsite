FROM python:3

COPY /home/pito/Desktop/Twins_project/TwinsWebsite/app/projects/SentimentAnalysis /home/pito/Desktop/Twins_project/TwinsWebsite/app

WORKDIR /app

RUN pip3 install -r requirments.txt 
RUN python -m nltk.downloader punkt
RUN python3 -m nltk.downloader wordnet
RUN python3 -m nltk.downloader stopwords

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]
