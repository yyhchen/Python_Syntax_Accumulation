在 Python 中，`get()` 方法主要用于从字典（dictionary）中获取指定键（key）对应的值（value）。以下是如何使用 `get()` 方法的示例：
```python
# 创建一个字典
person = {
    "name": "张三",
    "age": 25,
    "gender": "male"
}
# 使用 get() 方法获取指定键的值
name = person.get("name")
age = person.get("age")
gender = person.get("gender")
# 输出结果：
print(name)  # 输出：张三
print(age)   # 输出：25
print(gender)  # 输出：male
# 如果键不存在，get() 方法将返回默认值
unknown_key = person.get("unknown_key", "默认值")
# 输出结果：
print(unknown_key)  # 输出：默认值
```
注意：在使用 `get()` 方法时，如果指定的键不存在，将返回指定的默认值。如果没有提供默认值，则会报错。因此，建议在调用 `get()` 方法时传入默认值，以避免不必要的错误。