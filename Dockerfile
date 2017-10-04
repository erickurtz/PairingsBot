From python:3

ADD . /PairingsBot

WORKDIR /PairingsBot

RUN pip install -r requirements.txt

CMD ["python", "./BotApi/BotApi.py"]
