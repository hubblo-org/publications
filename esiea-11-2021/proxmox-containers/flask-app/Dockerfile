FROM debian:latest

MAINTAINER "My Self <myself@hello.none>"

WORKDIR app

RUN apt update -y

RUN apt install python3-flask -y

COPY . .

EXPOSE 5000/tcp

ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]

CMD ["-p", "5000"]
