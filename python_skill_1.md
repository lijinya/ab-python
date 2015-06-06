# Introduction #

python skill~

# Details #

  * 1. 求N 以内的素数...
```
from math import sqrt
# 求N 以内的素数...
from math import sqrt
N = 100
[ p for p in   range(2, N) if 0 not in [ p% d for d in range(2, int(sqrt(p))+1)] ]
^ ^  ^     ^               ^    ^      ^  ^              ^            ^      ^
| |  |     |               |    |      |  |              |            |      +- 弥补
| |  |     |               |    |      |  |              |            +- 通过平方精简尝试
| |  |     |               |    |      |  |              +- 组织所有 2~p 之间可能为公因子的数列
| |  |     |               |    |      |  +- 求余,尝试整除
| |  |     |               |    |      +- 列表运算,直接将以上计算结果组成数组 返回 
| |  |     |               |    +- 余数0 不在求余结果列表中
| |  |     |               +- 即2~p 都不能整除 p 的p
| |  |     +- 提取运算
| |  +- for..in 循环取数,从2~p 的连续数组中
| +- 素数!
+- 列表计算组织所有结果为数组返回!
# 优化::N > 10000 时可以使用 xrange() 进行优化生成数列
```

  * 2.实现两组数对调的效果  ，比如  1对5 2对6  3对7 4对8
> > php里只需要
```

$a=array('1','2','3','4');
$b=array('5','6','7','8');
$strnow='1234';
$new=preg_replace($a,$b,$strnow);
```
> > new就是5678
> > 但是re.sub肯定是不能这么批量实现的，怎么解决呢？
```
a = ['1', '2', '3', '4']
b = ['5', '6', '7', '8']
s = '1234'
```
```
# method1
import re
print re.sub('.', lambda m: dict(zip(a, b)).get(m.group(), m.group()), s)
# method2
print ''.join(dict(zip(a, b)).get(c, c) for c in s)
#method3
import string
print s.translate(string.maketrans(''.join(a), ''.join(b)))
```

  * 3.
```

特殊方法 描述
基本定制型
C.__init__(self[, arg1, ...]) 构造器（带一些可选的参数）
C.__new__(self[, arg1, ...]) 构造器（带一些可选的参数）；通常用在设置不变数据类
型的子类。
C.__del__(self) 解构器
C.__str__(self) 可打印的字符输出；内建str()及print 语句
C.__repr__(self) 运行时的字符串输出；内建repr() 和‘‘ 操作符
C.__unicode__(self)b Unicode 字符串输出；内建unicode()

C.__call__(self, *args) 表示可调用的实例
C.__nonzero__(self) 为object 定义False 值；内建bool() （从2.2 版开始）
C.__len__(self) “长度”（可用于类）；内建len()

特殊方法 描述
对象（值）比较c
C.__cmp__(self, obj) 对象比较；内建cmp()
C.__lt__(self, obj) and 小于/小于或等于；对应<及<=操作符
C.__gt__(self, obj) and 大于/大于或等于；对应>及>=操作符
C.__eq__(self, obj) and 等于/不等于；对应==,!=及<>操作符
属性
C.__getattr__(self, attr) 获取属性；内建getattr()；仅当属性没有找到时调用
C.__setattr__(self, attr, val) 设置属性
C.__delattr__(self, attr) 删除属性
C.__getattribute__(self, attr) 获取属性；内建getattr()；总是被调用
C.__get__(self, attr) （描述符）获取属性
C.__set__(self, attr, val)  （描述符）设置属性
C.__delete__(self, attr)  （描述符）删除属性
定制类/模拟类型
数值类型：二进制操作符
C.__*add__(self, obj) 加；+操作符
C.__*sub__(self, obj) 减；-操作符
C.__*mul__(self, obj) 乘；*操作符
C.__*div__(self, obj) 除；/操作符
C.__*truediv__(self, obj)  True 除；/操作符
C.__*floordiv__(self, obj)  Floor 除；//操作符
C.__*mod__(self, obj) 取模/取余；%操作符
C.__*divmod__(self, obj) 除和取模；内建divmod()
C.__*pow__(self, obj[, mod]) 乘幂；内建pow();**操作符
C.__*lshift__(self, obj) 左移位；<<操作符
特殊方法 描述
定制类/模拟类型
数值类型：二进制操作符

C.__*rshift__(self, obj) 右移；>>操作符
C.__*and__(self, obj) 按位与；&操作符
C.__*or__(self, obj) 按位或；|操作符
C.__*xor__(self, obj) 按位与或；^操作符
数值类型：一元操作符
C.__neg__(self) 一元负
C.__pos__(self) 一元正
C.__abs__(self) 绝对值；内建abs()
C.__invert__(self) 按位求反；~操作符
数值类型：数值转换
C.__complex__(self, com) 转为complex(复数);内建complex()
C.__int__(self) 转为int;内建int()
C.__long__(self) 转为long；内建long()
C.__float__(self) 转为float；内建float()
数值类型：基本表示法（String）
C.__oct__(self) 八进制表示；内建oct()
C.__hex__(self) 十六进制表示；内建hex()
数值类型：数值压缩
C.__coerce__(self, num) 压缩成同样的数值类型；内建coerce()
C.__index__(self)g 在有必要时,压缩可选的数值类型为整型（比如：用于切片
索引等等

序列类型
C.__len__(self) 序列中项的数目
C.__getitem__(self, ind) 得到单个序列元素
C.__setitem__(self, ind,val) 设置单个序列元素
C.__delitem__(self, ind) 删除单个序列元素
特殊方法 描述
序列类型
C.__getslice__(self, ind1,ind2) 得到序列片断
C.__setslice__(self, i1, i2,val) 设置序列片断
C.__delslice__(self, ind1,ind2) 删除序列片断
C.__contains__(self, val) f 测试序列成员；内建in 关键字
C.__*add__(self,obj) 串连；+操作符
C.__*mul__(self,obj) 重复；*操作符
C.__iter__(self)  创建迭代类；内建iter()

映射类型
C.__len__(self) mapping 中的项的数目
C.__hash__(self) 散列(hash)函数值
C.__getitem__(self,key) 得到给定键(key)的值
C.__setitem__(self,key,val) 设置给定键(key)的值
C.__delitem__(self,key) 删除给定键(key)的值
C.__missing__(self,key) 给定键如果不存在字典中，则提供一个默认值

```

  * 4.Python内置了一些非常有趣但非常有用的函数，充分体现了Python的语言魅力！


> filter(function, sequence)：对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决

于sequence的类型）返回：
```

>>> def f(x): return x % 2 != 0 and x % 3 != 0
>>> filter(f, range(2, 25))
[5, 7, 11, 13, 17, 19, 23]

>>> def f(x): return x != 'a'
>>> filter(f, "abcdef")
'bcdef'
```
map(function, sequence) ：对sequence中的item依次执行function(item)，见执行结果组成一个List返回：

```
>>> def cube(x): return x*x*x
>>> map(cube, range(1, 11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

>>> def cube(x) : return x + x
...
>>> map(cube , "abcde")
['aa', 'bb', 'cc', 'dd', 'ee']

```

另外map也支持多个sequence，这就要求function也支持相应数量的参数输入：
```

>>> def add(x, y): return x+y
>>> map(add, range(8), range(8))
[0, 2, 4, 6, 8, 10, 12, 14]
```

reduce(function, sequence, starting\_value)：对sequence中的item顺序迭代调用function，如果有starting\_value，还可以作为初始值调

用，例如可以用来对List求和：
```

>>> def add(x,y): return x + y
>>> reduce(add, range(1, 11))
55 （注：1+2+3+4+5+6+7+8+9+10）

>>> reduce(add, range(1, 11), 20)
75 （注：1+2+3+4+5+6+7+8+9+10+20）

```

lambda：这是Python支持一种有趣的语法，它允许你快速定义单行的最小函数，类似与C语言中的宏，这些叫做lambda的函数，是从LISP借用来的，可以用在任何需要函数的地方：
```
>>> g = lambda x: x * 2 
>>> g(3)
6
>>> (lambda x: x * 2)(3) 
6
```



  * 5
```
字典(dict)
dict 用 {} 包围 
dict.keys(),dict.values(),dict.items() 
hash(obj)返回obj的哈希值，如果返回表示可以作为dict的key 
del 或 dict.pop可以删除一个item,clear清除所有的内容 
sorted(dict)可以吧dict排序 
dict.get()可以查找没存在的key，dict.[]不可以 
dict.setdefault() 检查字典中是否含有某键。 如果字典中这个键存在，你可以取到它的值。 如果所找的键在字典中不存在，你可以给这个

键赋默认值并返回此值。 
{}.fromkeys()创建一个dict，例如: {}.fromkeys(('love', 'honor'), True) =>{'love': True, 'honor': True} 
不允许一个键对应多个值 
键值必须是哈希的，用hash()测试 
一个对象，如果实现_hash()_方法可以作为键值使用



集合(set)
集合是一个数学概念，用set()创建 
set.add(),set.update.set.remove，添加更新删除，-= 可以做set减法 
set.discard 和 set.remove不同在于如果删除的元素不在集合内，discard不报错，remove 报错 
< <= 表示 子集，> >=表示超集 
| 表示联合 & 表示交集 - 表示差集 ^ 差分集里啊



列表(list)
列表是序列对象，可包含任意的Python数据信息，如字符串、数字、列表、元组等。列表的数据是可变的，我们可通过对象方法对列表中的数

据进行增加、修改、删除等操作。可以通过list(seq)函数把一个序列类型转换成一个列表。
append(x) 在列表尾部追加单个对象x。使用多个参数会引起异常。 
count(x) 返回对象x在列表中出现的次数。 
extend(L) 将列表L中的表项添加到列表中。返回None。 
Index(x) 返回列表中匹配对象x的第一个列表项的索引。无匹配元素时产生异常。 
insert(i,x) 在索引为i的元素前插入对象x。如list.insert(0,x)在第一项前插入对象。返回None。 
pop(x) 删除列表中索引为x的表项，并返回该表项的值。若未指定索引，pop返回列表最后一项。 
remove(x) 删除列表中匹配对象x的第一个元素。匹配元素时产生异常。返回None。 
reverse() 颠倒列表元素的顺序。 
sort() 对列表排序，返回none。bisect模块可用于排序列表项的添加和删除。 



元组(tuple)
tuple=(1,)，这是单个元素的元组表示，需加额外的逗号。
tuple=1，2，3，4，这也可以是一个元组，在不使用圆括号而不会导致混淆时，Python允许不使用圆括号的元组。
和列表一样，可对元组进行索引、分片、连接和重复。也可用len()求元组长度。  
元组的索引用tuple[i]的形式，而不是tuple(i)。 
和列表类似，使用tuple(seq)可把其它序列类型转换成元组。
 

```