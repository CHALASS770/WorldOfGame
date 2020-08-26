FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /home/chal/PycharmProjects/test/requirements.txt

WORKDIR /home/chal/PycharmProjects/test

RUN pip install -r requirements.txt

COPY . /home/chal/PycharmProjects/test

ENTRYPOINT [ "python" ]

CMD [ "MainScore.py" ]
