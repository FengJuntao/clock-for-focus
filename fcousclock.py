import time

# 提醒用户专注的消息
print("请开始专注工作！")

# 25分钟的计时器
for i in range(25, -1, -1):
    # 显示剩余时间
    print(f"剩余时间：{i:02d} 分钟", end="\r")
    # 暂停 1 分钟
    time.sleep(60)

# 完成时提醒用户
print("\n恭喜，你已经完成了 25 分钟的工作！")
