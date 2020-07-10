import configparser
import os

config_path = os.path.join(os.getcwd(), '..', 'conf/config.ini')    # 获取配置文件的路径

# 封装配置文件类
class configUtils():
    def __init__(self,config_path = config_path):   # 初始化配置读取配置文件
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path)      # 读取配置文件

# 封装读取配置文件值的方法，便于后期扩展
#     @property
    def read_config(self,key,value):
        self.value = self.cfg.get(key, value)        # 根据配置文件中的键来获取值
        return self.value

configUtils = configUtils()     # 在封装模块中创建配置文件类的对象，这样在其他地方调用类的时候就不需要封装了

if __name__ == '__main__':      # 必须要有自测，不然后面麻烦的是自己
    hosts = configUtils.read_config('path', 'log_path')
    print(hosts)