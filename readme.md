## Basic Project-python 기반 추론 서버

### DB 접속 환경변수 필요

HOST='your_host'
DB='your_db'
USERNAME='your_name'
PORT='your_port'
PASSWORD='your_password'

### db test table 생성 필요

```
CREATE TABLE tb_test (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255)
);
```

### logging

root_path : /app/config/loginfo.json

- "root": "/app/logs"

log level : /app/utils/logger.py

- LOGGER.setLevel(logging.INFO)
