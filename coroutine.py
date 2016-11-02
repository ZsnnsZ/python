def consumer():
    r = ''
    while True:
        print('r---->%s' % r) #启动后执行到这里，遇见yield暂停
        n = yield r  #接受到n后执行
        if not n:
            print('a')
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    m = c.send(None) #负责启动生成器
    print('m == %s' % m)  
    n = 0
    while n < 1:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  #将n发送给c
        print('[PRODUCER] Consumer return: %s' % r)
        # next(c)
    c.close()

c = consumer()
produce(c)
