FROM python:3

ENTRYPOINT bash

ENV VENV_REQUIREMENTS "/tmp/requirements.pip"
COPY requirements.pip $VENV_REQUIREMENTS
RUN pip install --upgrade -r $VENV_REQUIREMENTS
