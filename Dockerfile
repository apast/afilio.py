FROM python:3

ENTRYPOINT bash

COPY requirements.pip /tmp/requirements.pip
RUN pip install /tmp/requirements.pip
