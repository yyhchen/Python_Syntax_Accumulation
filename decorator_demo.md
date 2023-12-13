# 更新下怎么使用装饰器
在Python中，装饰器是一种用来修改函数或方法的工具，通常用于在不修改原始代码的情况下添加新的功能或行为。装饰器本质上是一个函数，**它接受一个函数作为参数并返回一个新的函数**，从而实现对原始函数的包装。

以下是一个简单的装饰器例子：

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # 调用原始函数
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# 调用被装饰后的函数
say_hello()
```



在上面的例子中，`my_decorator` 是一个简单的装饰器，它接受一个函数 `func` 作为参数，并返回一个新的函数 `wrapper`。这个新函数在调用原始函数之前和之后输出一些额外的信息。使用 `@my_decorator` 语法将装饰器应用到函数 `say_hello` 上，这等同于 `say_hello = my_decorator(say_hello)`。

运行上述代码，输出将是：

```
    Something is happening before the function is called.
    Hello!
    Something is happening after the function is called.
```



这个例子中，装饰器 `my_decorator` 在调用 `say_hello` 函数前后添加了额外的逻辑。
