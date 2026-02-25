FROM ubuntu:22.04

WORKDIR /app

# Install netcat (HTTP listener tool)
RUN apt-get update && \
    apt-get install -y netcat-openbsd && \
    apt-get clean

# Expose backend port
EXPOSE 8080

# Start HTTP response loop
CMD while true; do \
  echo -e "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nServed by backend: $(hostname)" \
  | nc -l -p 8080 -q 1; \
done
