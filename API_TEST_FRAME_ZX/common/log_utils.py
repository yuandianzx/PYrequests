import logging
import os
import time
from API_TEST_FRAME_ZX.common.config_utils import configUtils

class Logger():
    def __init__(self):
        self.log_name = os.path.join(configUtils.read_config('path','log_path'), time.strftime("%Y-%m-%d") + 'test_log.txt')     # 拼接路径和文件名，将日志打印只logs目录下面
        self.getLogger = logging.getLogger()         # 创建一个getLogger对象，括号中可以选择带name参数，不输入默认为root
        self.getLogger.setLevel(logging.WARNING)     # 设置打印日志的级别，大于等于warning级别的日志会打印出来
        # print(log_path)

        self.console_handler = logging.StreamHandler()      # 打印日志至命令行
        self.file_handler = logging.FileHandler(self.log_name,'a',encoding='utf-8')        # 打印日志至log_name文件中，a表示追加

        self.formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")    # 设置打印日志的格式
        self.console_handler.setFormatter(self.formatter)        # 将console_handler的日志格式设置为formatter
        self.file_handler.setFormatter(self.formatter)
        self.getLogger.addHandler(self.console_handler)          # 将console_handler添加至getLogger对象中
        self.getLogger.addHandler(self.file_handler)
        self.console_handler.close()        # 关闭，避免重复打印
        self.file_handler.close()

    def get_logger(self):
        return self.getLogger

logger = Logger().get_logger()   # 直接创建日志对象，注意类名、方法名、变量名不可相同，负责调用的时候会出现问题。命名要规范！

if __name__ == '__main__':
    logger.warning('2')




