FROM python:3.6

ENV APP_PATH=/app/icons
WORKDIR $APP_PATH
RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./ ./
CMD [ "python", "main.py" ]
