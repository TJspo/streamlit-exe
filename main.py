import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.3)

'Done!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1解答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2解答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3解答')

# text = st.text_input('あなたの趣味を教えて下さい。')
# 'あなたの趣味:', text

# condition = st.slider('あなたの今の調子は', 0, 100, 50)
# 'あなたの今の調子は', condition


# st.sidebar.write('Interactive Widgets')

# text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
# 'あなたの趣味:', text

# condition = st.sidebar.slider('あなたの今の調子は', 0, 100, 50)
# 'あなたの今の調子は', condition


# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい、',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、', option,'です。'

# img = Image.open('/Users/tajiriwa/Desktop/mona-tatsu/mona/E77_トランペット.jpg')
# img = Image.open(E77_トランペット.jpg)

# if st.checkbox('Show Image'):
#     img = Image.open('mona.png')
#     st.image(img, caption='100m Truck', use_column_width=True)

# st.write('DataFrame')
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

# st.write(df)
# st.bar_chart(df)

# st.write(df, width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
# st.table(df.style.highlight_max(axis=0))

# """
# # 1
# ## (1)
# ### ①
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """





