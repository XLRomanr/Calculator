import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import requests
import time
from threading import Thread

def update_access_time():
    appid = "Plot_definition"  # 你应该替换成该 Streamlit 应用的 ID
    flask_server_url = "http://11.2.171.248:5000"  # 改成你的 Flask 服务器 IP
    url = f"{flask_server_url}/api/apps/{appid}/update_access_time"
    
    try:
        response = requests.post(url)
        if response.status_code == 200:
            st.success("访问时间已更新")
        else:
            st.warning("无法更新访问时间")
    except Exception as e:
        print(f"Failed to update access time: {e}")

# 后台线程定时调用更新访问时间
def run_periodic_update():
    while True:
        update_access_time()
        time.sleep(600)  # 每 10 分钟更新一次访问时间

# 启动后台线程（守护线程）
Thread(target=run_periodic_update, daemon=True).start()
# 设置页面标题
st.title("简单计算器")

# 用户输入
num1 = st.number_input("请输入第一个数字", value=0)
num2 = st.number_input("请输入第二个数字", value=0)

# 操作选择
operation = st.selectbox("选择运算符", ["加", "减", "乘", "除"])

# 计算并显示结果
if operation == "加":
    result = num1 + num2
elif operation == "减":
    result = num1 - num2
elif operation == "乘":
    result = num1 * num2
elif operation == "除":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "除数不能为零"

# 显示计算结果
st.write(f"结果是：{result}")
