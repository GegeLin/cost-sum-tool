# 导入需要的工具（和 Jupyter 里导入库一样）
import streamlit as st
import pandas as pd

# 1. 设置网页标题（浏览器里显示的标题）
st.title("消费数据求和工具")

# 2. 创建文件上传框（让用户上传 CSV）
st.subheader("第一步：上传你的 CSV 文件")
uploaded_file = st.file_uploader("点击选择 CSV 文件（仅含 cost 列）", type="csv")

# 3. 如果用户上传了文件，就开始处理
if uploaded_file is not None:
    # 读取上传的 CSV（和 pandas 读文件一样）
    df = pd.read_csv(uploaded_file)
    
    # 显示上传的数据预览（让用户确认上传对了）
    st.subheader("上传的数据预览")
    st.write(df.head(5))  # 像 Jupyter 里打印数据一样
    
    # 检查是否有 cost 列（防止用户传错文件）
    if "cost" not in df.columns:
        st.error("错误：上传的 CSV 里没有 'cost' 列！请重新上传正确的文件。")
    else:
        # 核心计算：对 cost 列求和（和 Jupyter 里的 pandas 语法完全一样）
        total_cost = df["cost"].sum()
        
        # 显示计算结果（让用户看到总和）
        st.subheader("计算结果")
        st.write(f"所有消费的总和 = {total_cost:.2f} 元")  # 保留两位小数，更直观
        
        # 4. 生成结果 CSV（包含总和数据）
        # 创建一个新的 DataFrame，存放结果（只有一行一列）
        result_df = pd.DataFrame({"消费总和（元）": [total_cost]})
        
        # 把结果转换成 CSV 格式（供下载）
        csv_result = result_df.to_csv(index=False, encoding="utf_8_sig")
        
        # 5. 创建下载按钮（用户点击就能保存到本地）
        st.subheader("第二步：下载结果")
        st.download_button(
            label="点击下载求和结果 CSV",
            data=csv_result,
            file_name="消费总和结果.csv",  # 下载后的文件名
            mime="text/csv"  # 文件类型
        )