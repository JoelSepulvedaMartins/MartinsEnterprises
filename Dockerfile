FROM python:3.11.3-alpine3.18

LABEL maintainer="luizomf@gmail.com"

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

RUN chmod +x /scripts/commands.sh

RUN chmod +x /scripts
RUN apk add --no-cache bash
RUN apk --no-cache add dos2unix

# Converter scripts para formato Unix/Linux
# RUN find /scripts -type f -exec dos2unix {} \;
# RUN find /djangoapp -type f -exec dos2unix {} \;

RUN find /scripts -exec dos2unix {} \;

RUN find /djangoapp -exec dos2unix {} \;


ENV PATH="/scripts:/venv/bin:$PATH"

#CMD ["sh", "-c", "tail -f /dev/null"]

#CMD ["ash", "-c", "ls -la /scripts && ls -la /djangoapp && pwd && /scripts/commands.sh"]

CMD ["sh", "-c", "ls -la /scripts && ls -la /djangoapp && pwd && /scripts/commands.sh"]

# # Adicionando o script diretamente ao Dockerfile
# RUN /bin/sh -c ' \
#     set -e; \
#     while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do \
#         echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."; \
#         sleep 2; \
#     done; \
#     echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"; \
#     python manage.py collectstatic; \
#     python manage.py migrate; \
#     python manage.py runserver \
# '