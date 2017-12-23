#!/bin/bash
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"

while ! pg_isready -h "postgres" -p "5432" > /dev/null 2> /dev/null; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 5
done

>&2 echo "Postgres is up - executing command"
exec $cmd