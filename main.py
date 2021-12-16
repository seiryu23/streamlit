import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image


st.title ('Streamlit 入門')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')


st.write('プログレスバーを表示')
'START'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i +1)
    time.sleep(0.05)

'DONE'
#sidebarでウィジェットから表示できる
#condition = st.sidebar.slider('あなたの今の調子は？', 0, 10, 5)
#text = st.sidebar.text_input('あなたの趣味を教えてください')

#st.write('コンディション', condition)
#st.write('あなたの趣味', text)

st.write('Display Image')

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)

st.write('あなたが好きな数字は、', option, 'です。')

#チェックボックス
if st.checkbox('Show Image'):
    img = Image.open('C:/Users/Seiryu/Desktop/Unity素材/moriBall/Ball0.png')
    st.image(img, caption='Uehata Seiryu', use_column_width=True)




#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#    columns=['lat', 'lon']
#)

#マップ表示
#st.map(df)

#df = pd.DataFrame(
#    np.random.rand(20, 3),
#    columns=['a','b', 'c']
#)
#df

#グラフ作成
#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)

#df = pd.DataFrame({
#'1列目':[1,2,3,4],
#'2列目':[11,22,33,44]
#})
# コメント
#st.dataframe(df.style.highlight_max(axis=0), width = 100, height = 100)
#st.dataframe(df.style.highlight_max(axis=0))
#st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""