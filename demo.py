import numpy as np
import pandas as pd
import streamlit as st

# 東京駅を中心に擬似的な位置情報データを生成する
lat, lon = 35.68184, 139.76718
df = pd.DataFrame(
    np.random.randn(1000, 2) / [100, 100] + [lat, lon],
    columns=['lat', 'lon']
)

st.title("位置情報 Web アプリを作成する最も簡単な方法")
st.subheader("Location Tech Advent Calendar 2021 by LBMA Japan")
st.map(df)
