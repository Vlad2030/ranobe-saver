gunicorn app:application --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8082 --log-level $1
