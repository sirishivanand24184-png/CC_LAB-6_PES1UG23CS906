FROM gcc:latest

WORKDIR /app

COPY app.cpp .

RUN g++ app.cpp -o app

RUN apt-get update && apt-get install -y netcat-openbsd

CMD while true; do echo -e "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n$(./app)" | nc -l -p 8080 -q 1; done
