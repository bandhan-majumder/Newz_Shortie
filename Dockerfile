FROM python:3.9-slim-buster as build

# Install Nginx and other dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends nginx iputils-ping libcap2 libidn2-0 libnettle6 libunistring2 && \
    rm -rf /var/lib/apt/lists/*

# Create app directory and copy requirements.txt
WORKDIR /app
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Copy Nginx configuration template and script
COPY nginx.conf.template /app/nginx.conf.template
COPY config_and_start_nginx.sh /app/config_and_start_nginx.sh
RUN chmod +x /app/config_and_start_nginx.sh

# Expose ports
EXPOSE 80 5000

# Final stage
FROM python:3.9-slim-buster

# Copy Nginx and application code
COPY --from=build /app /app

# Set working directory
WORKDIR /app

# Run Nginx and application script
CMD ["/app/config_and_start_nginx.sh"]
