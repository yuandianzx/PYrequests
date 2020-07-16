import logging
import os
import time
from config_utils import ConfigUtils

getLogger = logging.getLogger()         # 创建一个getLogger对象，括号中可以选择带name参数，不输入默认为root
getLogger.setLevel(logging.WARNING)     # 设置打印日志的级别，大于等于warning级别的日志会打印出来

daytime = time.strftime("%Y-%m-%d")     # 获取当前天数
log_path = os.path.join(ConfigUtils.read_config('path','log_path'), daytime + 'test_log.txt')       # 拼接路径和文件名，将日志打印只logs目录下面
# print(configUtils.read_config('path','log_path'))

handler1 = logging.StreamHandler()      # 打印日志至命令行
handler2 = logging.FileHandler(log_path,'a',encoding='utf-8')        # 打印日志至test_log文件中，a表示追加

formatter =  logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")    # 设置打印日志的格式
handler1.setFormatter(formatter)        # 将handler1的日志格式设置为formatter
handler2.setFormatter(formatter)
getLogger.addHandler(handler1)          # 将handler1添加至getLogger对象中
getLogger.addHandler(handler2)


getLogger.debug('这是一个debug日志信息')
getLogger.info('这是一个info日志信息')
getLogger.warning('这是一个warning日志信息')
getLogger.error('这是一个error日志信息')
logging.critical('这是一个critical日志信息')


