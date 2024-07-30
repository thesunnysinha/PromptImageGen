script_directory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "$script_directory/backend"

celery -A main worker --loglevel=info -c 6

