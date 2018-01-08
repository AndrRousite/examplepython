# pythonexample as python 3.6.4

###### 集成环境
```angular2html
Python是跨平台的，它可以运行在Windows、Mac和各种Linux/Unix系统上。
IDE: PyCharm,eclipse,IDEA 
python 解释器：
    1. CPython(C语言开发的)
    2. PyPy，采用JIT技术，对Python代码进行动态编译
    3. Jython是运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。
    4. IronPython是运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。
```

###### 基础语法
```angular2html
%运算符用来格式化字符串:
    %d	整数
    %f	浮点数
    %s	字符串
    %x	十六进制整数
条件判断: if elif else
循环：for...in / while循环
```

###### 数据类型
```angular2html
list(列表): 可变的有序列表: 定义 []
tuple(元组): 不可变的有序列表： 定义(1,)
dict(字典): key必须是不可变对象，一个key只能对应一个value的无序map集合，使用键-值（key-value）存储，具有极快的查找速度
set: 无序和无重复元素的集合，set和dict类似，也是一组key的集合，但不存储value。set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

特性：
    1. 切片
    2. 迭代
    3. 列表生成式：>>>[x * x for x in range(1, 11)]        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    4. 生成器(generator)
    5. 迭代器
    for循环的数据类型有以下几种：
        一类是集合数据类型，如list、tuple、dict、set、str等；
        一类是generator，包括生成器和带yield的generator function。
    这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
    生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
    为什么list、dict、str等数据类型不是Iterator？
        因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
        Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
        
```

###### 函数和模块
```angular2html
1. 函数别名： 
    a = abs      # 变量a指向abs函数
    print(a(-1)) # 所以也可以通过a调用abs函数
2. 定义函数：
    def funcName():
        pass 
3. 高阶函数:
    把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
    1. map: 接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
    2. reduce: 一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是： reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    3. filter: 用于过滤序列,和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素，并把结果作为新的Iterator返回。
    4. sorted: 排序算法
4. 返回函数：闭包,实现懒加载,闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
5. 匿名函数：关键字lambda表示匿名函数，冒号前面的x表示函数参数。
6. 装饰器：扩展函数，可以是一个函数名同时指向多个函数，调用多个函数
7. 偏函数：对于重载函数，起别名，调用方便

模块：
    为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。
    一个.py文件就是一个模块
    安装第三方模块：
        pip：包管理器
        常用的第三方模块：
            Pillow:图形处理
            requests:http请求
            chardet:字符编码
            psutil:获取系统信息
    常用内建模块：
        datetime：
            datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
            如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
        collections:
            Python内建的一个集合模块，提供了许多有用的集合类。
        base64:
            一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
        hashlib:
            提供了常见的摘要算法，如MD5，SHA1等等。
        hmac:
            hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。
        itertools:
            提供了非常有用的用于操作迭代对象的函数
        urllib:
             一系列用于操作URL的功能。   
        json:
        xml:
        HTMLParser:
            HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
            Python提供了HTMLParser来非常方便地解析HTML
            
```

###### 面向对象编程
```angular2html
封装、继承和多态
    类和实例：
        实例属性属于各个实例所有，互不干扰；
        类属性属于类所有，所有实例共享一个属性；
    __slots__：限制实例的属性
    @property: 检查参数
    多重继承：
    定制类：
        __str__:
        __iter__:
        ......
    枚举类：
    元类：
```

###### 错误、调试和测试
```angular2html
有的错误是程序编写有问题造成的，比如本来应该输出整数结果输出了字符串，这种错误我们通常称之为bug，bug是必须修复的。

有的错误是用户输入造成的，比如让用户输入email地址，结果得到一个空字符串，这种错误可以通过检查用户输入来做相应的处理。

还有一类错误是完全无法在程序运行过程中预测的，比如写入文件的时候，磁盘满了，写不进去了，或者从网络抓取数据，网络突然断掉了。这类错误也称为异常，在程序中通常是必须处理的，否则，程序会因为各种问题终止并退出。

异常：
    try:
        pass
    except: BaseException as e :
        pass
    else:
        pass
    finally:
        pass
        
        
抛出自定义的异常：
    raise ? extends BaseException('')
    raise:可以不带参数，则原样抛出   
    
调试：
    1. print打印日志    (最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。)
    2. 断言：assert ...  (如果断言失败，assert语句本身就会抛出AssertionError,启动Python解释器时可以用-O参数来关闭assert,关闭后，你可以把所有的assert语句当成pass来看。)       
    3. logging  (logging可以定义日志级别，logging不会抛出错误，而且可以输出到console和文件)
    4. 断点：启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。

单元测试：   

文档测试：
    
```

###### 文件I/O和异常处理
```angular2html
打开文件： open()
关闭文件： close()
读文件：   read()
写文件：   write()

StringIO和BytesIO

目录和文件操作：os模块和os.path模块

序列化：程序运行的过程中，所有的变量都是在内存中，把变量从内存中变成可存储或传输的过程称之为序列化

JSON: 

```

###### CGI和网络编程
```angular2html
Socket:
    so easy 
    TCP 协议：s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    UDP 协议：s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
STMP: 发送邮件
POP3: 收取邮件   
```

###### 数据库存储
```angular2html
ORM 
```

###### Web开发
```angular2html
HTTP协议：
HTML：
WSGI接口：
WEB框架：
    Flask:
    Django：全能型Web框架；
    web.py：一个小巧的Web框架；
    Bottle：和Flask类似的Web框架；
    Tornado：Facebook的开源异步Web框架。
模板引擎：
    Jinja2:
    Mako：用<% ... %>和${xxx}的一个模板；
    Cheetah：也是用<% ... %>和${xxx}的一个模板；
    Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。
```

###### 多进程和多线程
```angular2html
多进程:
    在Unix/Linux下，可以使用fork()调用实现多进程。
    要实现跨平台的多进程，可以使用multiprocessing模块。
    进程间通信是通过Queue、Pipes等实现的。
多线程：
    多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
    Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
```

###### GUI编程(鸡肋)
```angular2html
Python(自带的库是支持Tk的Tkinter)支持多种图形界面的第三方库，包括：
    Tk
    wxWidgets
    Qt
    GTK
```

###### 异步IO
```chameleon

```

###### JSON和XML解析以及正则处理
    json:
    xml:

###### Python3.x和2.x版本区别



### 练习项目
1. 
