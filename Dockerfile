FROM python:3.10.0

RUN pip install click colorama flask sqlalchemy 'tweepy~=3.10'
RUN pip install git+https://github.com/micahflee/semiphemeral

ENTRYPOINT ["/usr/local/bin/semiphemeral"]