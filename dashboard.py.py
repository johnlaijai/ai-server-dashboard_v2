import streamlit as st
import yfinance as yf
import pandas as pd
from newsapi import NewsApiClient

# 標題設定
st.title("🚀 AI 伺服器戰情室")

# 這裡讀取你的 API Key (來自 Streamlit Cloud 的設定)
# 注意：在本地測試時，你需要改用 st.secrets["NEWSAPI_KEY"] 或直接貼上字串
news_api_key = st.secrets.get("NEWSAPI_KEY", "你的_API_KEY_字串")

# 簡單測試頁面
ticker = st.selectbox("選擇公司", ["DELL", "SMCI", "HPE"])
st.write(f"你正在分析：{ticker}")

# 範例：顯示股價
data = yf.Ticker(ticker).history(period="1d")
st.line_chart(data['Close'])

st.write("準備好將你的複雜邏輯放入這裡了！")