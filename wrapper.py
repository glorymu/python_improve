#装饰器的本质是一个包装函数，即函数运行前添加一些注释或者额外操作，
#但是会改变函数的__name__参数，因此需要functools辅助同时改变__name__参数
import functools,time

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*arg,**kw):
        print(123)
        print('%s executed in %s ms' % (fn.__name__, time.time()))
        return fn(*arg,**kw)
    return wrapper
# 测试
print('hello')


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)

s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')