# Use GCC image
FROM gcc:latest

# Set working directory
WORKDIR /app

# Copy source code
COPY app.cpp .

# Compile program
RUN g++ app.cpp -o app

# Expose port (for lab requirement)
EXPOSE 8080

# Run simple HTTP server loop
CMD while true; do \
      echo -e "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nServed by backend: $(hostname)" \
      | nc -l -p 8080 -q 1; \
    done
