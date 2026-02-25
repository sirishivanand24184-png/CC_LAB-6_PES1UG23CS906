FROM ubuntu:22.04

RUN apt-get update && apt-get install -y netcat hostname && apt-get clean

CMD while true; do \
  echo -e "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nConnection: close\r\n\r\nServed by backend: $(hostname)" \
  | nc -l -p 8080 -q 1; \
done
