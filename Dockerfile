FROM python:3.11
WORKDIR /project
COPY ./requirements.txt /project/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt
COPY ./app /project/app
