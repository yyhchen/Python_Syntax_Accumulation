from tqdm import tqdm
import time

# 模拟一个漫长的任务列表
tasks = range(100)

# 使用 tqdm 装饰器包装循环
with tqdm(total=len(tasks)) as pbar:
    for task in tasks:
        # 模拟执行任务
        time.sleep(0.5)

        # 更新进度条
        pbar.update(1)

print("All tasks completed.")

