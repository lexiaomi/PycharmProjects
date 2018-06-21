import logging

LOG_FORMAT = "%(asctime)s=====%(levelname)s+++++%(message)s"
logging.basicConfig(filename="lilijun.log", level=logging.DEBUG,format=LOG_FORMAT)
logging.debug("this is debug log")
logging.info("this is info log")
logging.warning("this is warning log")
logging.error("this is error log")
logging.critical("this is critical log")
format()
