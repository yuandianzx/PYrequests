import configparser
import os

config_path = os.path.join(os.getcwd(), '..', 'conf/config.ini')    # 获取配置文件的路径

# 封装配置文件类
class configUtils():
    def __init__(self,config_path = config_path):   # 初始化配置读取配置文件
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path)      # 读取配置文件

# 封装读取配置文件值的方法，便于后期扩展
    def read_config(self,key,value):
        self.value = self.cfg.get(key, value)        # 根据配置文件中的键来获取值
        return self.value
