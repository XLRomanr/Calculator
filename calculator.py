import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import requests
import time
from threading import Thread

def update_access_time():
    """ 访问 Streamlit 页面时调用后端 API 记录最后访问时间 """
    appid = "Calculator"  # 你的 Streamlit 应用 ID
    flask_server_url = "http://11.2.171.248:5000"  # 你的 Flask 服务器地址
    url = f"{flask_server_url}/api/apps/{appid}/update_access_time"

    try:
        response = requests.post(url)
        if response.status_code == 200:
            st.success("访问时间已更新")
        else:
            st.warning("无法更新访问时间")
    except Exception as e:
        st.error(f"更新访问时间失败: {e}")

# **只在用户首次进入页面（当前会话）时调用**
if "access_logged" not in st.session_state:
    update_access_time()
    st.session_state.access_logged = True  # 标记当前会话已记录访问时间
    
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
