FROM python:3.8.0-buster



ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry

WORKDIR /APPS/nodo
#VOLUME . /APPS/blockchain

COPY . /APPS/nodo

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction
RUN apt-get-update install curl
RUN apt-get install net-tools
CMD ["python", "api.py"]




