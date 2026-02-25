FROM ubuntu:22.04

RUN apt-get update && apt-get install -y netcat-openbsd hostname && apt-get clean

CMD while true; do \
  RESPONSE="Served by backend: $(hostname)"; \
  printf "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: ${#RESPONSE}\r\nConnection: close\r\n\r\n$RESPONSE" \
  | nc -lk -p 8080 -q 0; \
done
