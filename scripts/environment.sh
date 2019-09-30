#!/bin/bash -e

if [ -f ./.venv/bin/activate ]; then
    echo "Load Python virtualenv from './.venv/bin/activate'"
    . ./.venv/bin/activate
fi
exec "$@"