#filter的本质是过滤器，将不满足函数条件的数剔除，不仅可以修饰数组
#还可以修饰生成器，同时可以套多重过滤器,返回的也是生成器
#map函数同理，不过不是过滤而是映射
#lambda x:f(x)  无名函数，

#yield 一个方法变成了一个生成器，很有意思

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列



# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break        