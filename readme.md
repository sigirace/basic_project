## Basic Project

### python 기반 추론 서버

1. mysql
2. datahandler
3. logging

### .env file 생성 필요

HOST='your_host'
DB='your_db'
USERNAME='your_name'
PORT='your_port'
PASSWORD='your_password'

### db test table 생성 필요

CREATE TABLE tb_test (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255)
);

### logging

root_path : config/loginfo.json

- "root": "./logs"

log level : utils/logger.py

- LOGGER.setLevel(logging.INFO)
