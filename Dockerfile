FROM debian:buster-slim AS build
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes \
    python3-venv gcc libpython3-dev iputils-ping libcap2 libunistring2 libidn2-0 libnettle6 nginx && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip
    
# Install Python dependencies
FROM build AS build-venv
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

# Final stage
FROM debian:buster-slim
RUN apt-get update && apt-get install -y --no-install-recommends bash python3
COPY --from=build-venv /venv /venv
COPY --from=build-venv /bin/ping /bin/ping
COPY --from=build-venv /lib/x86_64-linux-gnu/libcap.so.2 /lib/x86_64-linux-gnu/libcap.so.2
COPY --from=build-venv /usr/lib/x86_64-linux-gnu/libidn2.so.0 /usr/lib/x86_64-linux-gnu/libidn2.so.0
COPY --from=build-venv /usr/lib/x86_64-linux-gnu/libnettle.so.6 /usr/lib/x86_64-linux-gnu/libnettle.so.6
COPY --from=build-venv /usr/lib/x86_64-linux-gnu/libunistring.so.2 /usr/lib/x86_64-linux-gnu/libunistring.so.2

# Copy Nginx and its dependencies
COPY --from=build-venv /usr/sbin/nginx /usr/sbin/nginx
COPY --from=build-venv /usr/lib/nginx /usr/lib/nginx
COPY --from=build-venv /etc/nginx /etc/nginx
COPY --from=build-venv /var/log/nginx /var/log/nginx
COPY --from=build-venv /var/lib/nginx /var/lib/nginx
COPY --from=build-venv /usr/share/nginx /usr/share/nginx

# Copy application
COPY . /app
WORKDIR /app

# Copy Nginx configuration template and script
COPY nginx.conf.template /app/nginx.conf.template
COPY config_and_start_nginx.sh /app/config_and_start_nginx.sh

RUN pwd && ls -la && sleep 20
RUN chmod +x config_and_start_nginx.sh

EXPOSE 80
EXPOSE 5000

# use config_and_start_nginx.sh script as entrypoint
ENTRYPOINT ["/app/config_and_start_nginx.sh"]
