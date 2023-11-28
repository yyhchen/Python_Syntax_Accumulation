# multiprocessing库 中的 Manger（）函数

**示例代码**：

```python{.line-numbers}
    if self.parallel:
            with Manager() as manager:      # python自带的多进程类，添加这行代码是为了确保多进程运行时 能够正确使用共享的数据结构
                pool = Pool(self.num_cpu)
                if self.is_pdf:
                    print('Running PDF analysis')
                else:
                    print('Running XRD analysis')
                # 这里的imap是为每个进程分配任务，第一个参数是函数；第二个参数表示的是输入。必须是可迭代的数据结构
                all_info = list(tqdm(pool.imap(self.classify_mixture, spectrum_filenames),
                    total=len(spectrum_filenames)))     # 显示进度条

        else:
            all_info = []
            for filename in spectrum_filenames:
                all_info.append(self.classify_mixture(filename))
```

这里的 `with Manger as manger:` 不能删除

在这段代码中，`with Manager() as manager:` 语句创建了一个使用 `multiprocessing` 模块的 `Manager` 对象。`Manager` **对象用于创建共享的对象和命名空间，以便在多个进程之间共享数据。**

在这里，主要用到了 `Manager` 的作用是创建了一个共享的 `manager` 对象，以确保在多个进程中能够正确地使用共享的数据结构。在多进程编程中，由于每个进程有自己的地址空间，因此需要通过特殊的机制来共享数据。`Manager` 提供了一种方式，可以创建共享的数据结构，例如 `list`、`dict` 等。

如果你删除了这行代码，可能会导致在多进程运行时出现一些问题，因为共享的数据结构可能无法正确同步。所以，**保留 `with Manager() as manager:` 是为了确保在多进程运行时能够正确地使用共享的数据结构，从而避免潜在的问题。**

总的来说，不建议删除这行代码，除非你有其他合适的方式来处理多进程共享数据的情况。