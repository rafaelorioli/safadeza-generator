FROM python:3.7

RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt

RUN pip install -r /tmp/requirements.txt

ENV consumer_key=''
ENV consumer_secret=''

ENV access_token=''
ENV access_token_secret=''


COPY . /app
WORKDIR /app
CMD python main.py