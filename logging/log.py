# 学习使用 logging 模块
# !!! 该模块/不/应该在 Jupyter 等交互式的 python 环境下进行学习

# logger --> handler --> filter，这 3 个是 logging 常用的对象，
# 3 者控制能力的颗粒度从左至右越来越精细

# 有两种方法可以配置 logging
# 1. `logging.basciConfig`，全局配置
# 2. 设置 logger 等对象的属性，设置得更为细致，如
#       logger.setFormatter
#       logger.setLevel

import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)  # 设置全局的日志 level

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  # 设置输出格式

# FileHandler
file_handler = logging.FileHandler('my.log')  # 将日志输出到文件 my.log
file_handler.setFormatter(formatter)  # 将设置好的 formatter 塞入 handler
logger.addHandler(file_handler)

# StreamHandler
stream_handler = logging.StreamHandler()  # 将日志输出到控制台
stream_handler.setLevel(logging.ERROR)  # 控制台的日志 Level 提高到 Error
stream_handler.setFormatter(formatter)  # 同样将设置好的 formatter 塞入 handler
logger.addHandler(stream_handler)

# log
logger.info('Strat')
logger.warning('There is something wrong.')
try:
    result = 10 / 0
except Exception:
    logger.error('Failed', exc_info=True)
logger.info('End\n')

# 参考资料
# - [PyTorch 29.Python 日志库 logging](https://zhuanlan.zhihu.com/p/166236399)
# - [python中logging模块上篇](https://zhuanlan.zhihu.com/p/38781838)
# - [python中logging模块下篇](https://zhuanlan.zhihu.com/p/38782314)

# 待完善
# - 学习配置共享以及配置到文件 (.ymal)
# - 日志级别的设置
# - RotatingFileHandler 防止日志文件越来越大
# - 更细致的 filter 对象使用
