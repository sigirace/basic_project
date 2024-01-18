FROM --platform=linux/amd64 python:3.10.13-slim

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && \
    apt-get install -y vim wget bzip2 curl git build-essential&& \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#  apt-get upgrade 
#  python3-capstone libpq-dev 

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app

EXPOSE 80

# CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "main:app"]

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:80", "--workers", "4", "--threads", "4", "--timeout", "1000"]
