import json
import os
import logging
from datetime import datetime

PATH_LOG_INFO = "src/config/logInfo.json"

def get_logger():

    with open(PATH_LOG_INFO, "r", encoding="utf-8") as fp:
        LOG_INFO = json.load(fp)

    FORMAT_STRING = LOG_INFO["format"]
    ROOT_LOG = LOG_INFO["root"]
    FNAME_LOG = LOG_INFO["name"]

    # 월별 로그 파일 네임 생성
    current_month = datetime.now().strftime("%Y_%m")  # 현재 날짜의 연도와 월을 포함하는 문자열
    FPATH_LOG = "{}/{}_{}.log".format(ROOT_LOG, FNAME_LOG, current_month)

    # ROOT Folder가 없으면 생성
    if not os.path.exists(ROOT_LOG):
        os.mkdir(ROOT_LOG)

    # 로그 생성
    LOGGER = logging.getLogger()

    # 로그의 출력 기준 설정
    LOGGER.setLevel(logging.INFO)

    # 로그 출력 형식
    formatter = logging.Formatter(FORMAT_STRING)

    # 로그 콘솔 출력
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    LOGGER.addHandler(stream_handler)

    # 로그 파일 핸들러 추가
    file_handler = logging.FileHandler(FPATH_LOG)
    file_handler.setFormatter(formatter)
    LOGGER.addHandler(file_handler)

    return LOGGER