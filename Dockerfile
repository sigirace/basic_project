FROM basic_project:0.0.1

COPY app /app

EXPOSE 8080

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8080", "--workers", "4", "--threads", "4", "--timeout", "1000"]
