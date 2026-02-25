FROM gcc:latest

WORKDIR /app

COPY app.cpp .

RUN g++ app.cpp -o app

CMD ["sh", "-c", "while true; do ./app | nc -l -p 8080 -q 1; done"]
