#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e
apk add --no-cache bash
apk --no-cache add dos2unix
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"


python manage.py collectstatic --noinput

python manage.py makemigrations --noinput
echo 'Executando migrate.sh'
python manage.py migrate --noinput

python manage.py runserver 0.0.0.0:8000


# wait_psql.sh
# collectstatic.sh
# migrate.sh
# runserver.sh
