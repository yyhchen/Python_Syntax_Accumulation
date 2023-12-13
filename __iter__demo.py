class SimpleIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        # 返回迭代器对象自身
        return self

    def __next__(self):
        # 定义迭代逻辑
        if self.current <= self.end:
            result = self.current
            self.current += 1
            yield result
        # else:
        #     # 当达到结束条件时，抛出 StopIteration 异常
        #     raise StopIteration

# 使用自定义迭代器
my_iterator = SimpleIterator(1, 5)

# 使用 for 循环遍历迭代器
# for num in my_iterator:
#     print(num)



class SimpleGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def generate_numbers(self):
        current = self.start
        while current <= self.end:
            yield current
            current += 1

# 使用生成器
my_generator = SimpleGenerator(1, 5)

# 使用 for 循环遍历生成器
# for num in my_generator.generate_numbers():
#     print(num)


class SimpleIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        # 在 __iter__ 方法中使用 yield
        current = self.start
        while current <= self.end:
            yield current
            current += 1

# 使用自定义迭代器
my_iterator = SimpleIterator(1, 5)

# 使用 for 循环遍历迭代器
for num in my_iterator:
    print(num)


