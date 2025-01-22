import streamlit as st

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
