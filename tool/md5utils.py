
import hashlib  # 推荐使用


def getMD5(file):
    '''参数是二进制数据'''
    m = hashlib.md5()  # 创建一个md5对象
    m.update(file)  # 将要md5的对象更新到md5中，字节类型参数
    return m.hexdigest()  # 生成一个md5摘要值
