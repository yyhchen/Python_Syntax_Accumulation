在 Python 中，`getattr()` 函数用于获取一个对象（如类、实例或模块）的属性或方法。该函数的语法如下：
```python
getattr(object, name[, default])
```
参数说明：
- `object`：要查询的对象。
- `name`：属性或方法的名称。可以使用字符串表示。
- `default`（可选）：当属性或方法不存在时，返回的默认值。如果未提供此参数，则在找不到属性或方法时会引发 `AttributeError`。

使用示例：
```python
# 定义一个类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
        
# 创建一个 Person 实例
person = Person("张三", 25)
# 使用 getattr() 获取实例的属性
name = getattr(person, "name")
age = getattr(person, "age")

# 输出结果：
print(name)  # 输出：张三
print(age)   # 输出：25

# 使用 getattr() 调用实例的方法
person.say_hello()  # 输出：Hello, my name is 张三 and I am 25 years old.

# 使用 getattr() 获取不存在的属性，默认值为空字符串
non_existent_attr = getattr(person, "non_existent_attr", "")

# 输出结果：
print(non_existent_attr)  # 输出：
```
在这个示例中，我们首先定义了一个 `Person` 类，然后创建了一个 `Person` 实例。接下来，我们使用 `getattr()` 函数获取实例的属性 `name` 和 `age`，以及调用其 `say_hello()` 方法。最后，我们尝试获取不存在的属性 `non_existent_attr`，并设置默认值为空字符串。