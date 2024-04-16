import streamlit as st
import numpy as np
import pandas as pd
import json
from PIL import Image

st.title("Streamlit 超入門")

st.write("DataFrame")

df = pd.DataFrame({
    "1列目": [1, 2, 3, 4],
    "2列目": [10, 20, 30, 40]
})

#st.write(df)
# 動的な表
st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)

# 静的な表
st.table(df.style.highlight_max(axis=0))

# 仮のJSONデータ
my_data = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "hobbies": ["reading", "traveling", "photography"]
}
#st.json(json.dumps(my_data, indent=4))
st.json(json.dumps(my_data))

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=["a", "b", "c"]
)
st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=["lat", "lon"]
)
st.map(df)

st.write("Display Image")

# checkboxを用いて画像を表示させるかどうか選択させる
if st.checkbox("Show Image"):
    img = Image.open("2.jpg")
    st.image(img, caption="nature", use_column_width=True)

# selectboxを用いて数字を選択させる
option = st.selectbox(
    "貴方が好きな数字を教えて下さい",
    list(range(1, 11))
)
"貴方が好きな数字", option

# textを反映させる
text = st.text_input("自動分類のためのカテゴリーを入力して下さい")
"カテゴリー：", text