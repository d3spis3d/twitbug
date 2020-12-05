FROM python:3.9-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV HANDLE Twitter

EXPOSE 8888

CMD python -u twitbug.py $HANDLE 0.0.0.0 8888