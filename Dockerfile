FROM python:3.11.6-alpine3.18

LABEL maintainer="joelsepulveda02@outlook.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY djangoapp /djangoapp
COPY scripts /scripts

WORKDIR /djangoapp

EXPOSE 8000


RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /djangoapp/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts



RUN apk add bash dos2unix
RUN apk add bash
RUN apk add dos2unix

# Converter scripts para formato Unix/Linux
RUN find /scripts -type f -exec dos2unix {} \;
RUN find /djangoapp -type f -exec dos2unix {} \;

RUN find /scripts -exec dos2unix {} \;

RUN find /djangoapp -exec dos2unix {} \;

RUN chmod +x /scripts/commands.sh

RUN chmod +x /scripts

ENV PATH="/scripts:/venv/bin:$PATH"



#CMD ["sh", "-c", "tail -f /dev/null"]

#CMD ["ash", "-c", "ls -la /scripts && ls -la /djangoapp && pwd && /scripts/commands.sh"]

CMD ["sh", "-c", "ls -la /scripts && ls -la /djangoapp && pwd && /scripts/commands.sh"]
# Muda o usuário para duser
#USER duser
