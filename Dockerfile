FROM alpine:3.8
MAINTAINER Werner Beroux <werner@beroux.com>

RUN set -x \
    # Install ngrok (latest official stable from https://ngrok.com/download).
 && apk add --no-cache curl \
 && curl -Lo /ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip \
 && unzip -o /ngrok.zip -d /bin \
 && rm -f /ngrok.zip \
    # Create non-root user.
 && adduser -h /home/ngrok -D -u 6737 ngrok
 
RUN set -x \
    # install python 3 and plexapi
 && apk add --no-cache python3 \
 && python3 -m ensurepip \
 && rm -r /usr/lib/python*/ensurepip \
 && pip3 install --upgrade pip setuptools \
 && if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi \
 && if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi \
 && rm -r /root/.cache \
 && pip3 install plexapi \
 && apk add nano

# Add config script.
COPY ngrok.yml /home/ngrok/.ngrok2/
COPY entrypoint.sh /
COPY plexurl.py /

USER ngrok
ENV USER=ngrok

EXPOSE 4040

CMD ["/entrypoint.sh"]
