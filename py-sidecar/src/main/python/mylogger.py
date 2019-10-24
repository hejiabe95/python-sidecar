import logging
import sys

def my_get_logger(appname):
    #获取logger实例，如果参数为空则返回root logger
    logger=logging.getLogger(appname)
    #创建日志输出格式
    formatter=logging.Formatter('%(asctime)s    %(levelname)s:  %(message)s')

    #指定输出的文件路径
    file_handler=logging.FileHandler('test.log')
    # 设置文件处理器，加载处理器格式
    file_handler.setFormatter(formatter)

    #控制台日志
    console_handler=logging.StreamHandler(sys.stdout)
    console_handler.formatter=formatter

    #为logger添加的日志处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    #指定日志的最低输出级别，默认为warn级别
    logger.setLevel(logging.INFO)
    return logger

logger=my_get_logger('python_test')