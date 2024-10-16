FROM python:3.12-slim

WORKDIR /app

COPY app.py .
COPY ./templates/ ./templates/

RUN pip install Flask psycopg2-binary

EXPOSE 8001

CMD [ "python", "app.py" ]