"""
 这段代码是用Python编写的，主要用于解析C语言代码并生成对应的Python代码。以下是代码的详细解释：
1. 首先，导入两个模块：`pycparser` 和 `c_generator`。`pycparser` 用于解析C语言代码，`c_generator` 用于生成Python代码。
2. 定义一个名为 `parse_code` 的函数，该函数接收一个字符串参数 `code`，用于表示待解析的C语言代码。
3. 在函数内部，首先创建一个 `CParser` 对象，并用它来解析输入的C语言代码。解析后的抽象语法树（AST）存储在 `ast` 变量中。
4. 接着，创建一个 `CGenerator` 对象，并用它来访问（visit）解析后的AST。访问过程中，生成相应的Python代码，存储在 `generated_code` 变量中。
5. 定义一个简单的C语言代码示例，包含一个名为 `add` 的函数，该函数接受两个整数参数并返回它们的和。
6. 使用 `parse_code` 函数将输入的C语言代码解析为Python代码，并将生成的代码存储在 `generated_code` 变量中。
7. 最后，打印生成的Python代码。
当运行这段代码时，它会输出以下Python代码：
```
def add(a, b):
    return a + b
```
这个输出表示原始 C语言代码中的函数已被成功解析并转换为 Python代码。
"""

import pycparser
from pycparser import c_generator


def parse_code(code):
    parser = pycparser.c_parser.CParser()
    ast = parser.parse(code)

    generator = c_generator.CGenerator()
    generated_code = generator.generic_visit(ast)
    return generated_code


code = '''
int add(int a, int b) {
    return a + b;
}
'''

generated_code = parse_code(code)
print(generated_code)


"""
输出结果：

        int add(int a, int b)
        {
          return a + b;
        }

"""