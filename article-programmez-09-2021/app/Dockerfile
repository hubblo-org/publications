FROM python

RUN pip3 install -U Flask psycopg2

COPY . .

CMD ["flask", "run", "-h", "0.0.0.0"]
