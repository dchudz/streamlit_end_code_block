from end_code_block import end_code_block as _____
import streamlit as st
import pandas as pd
_____(display=False)

message = 'hello world'
st.write(message)
_____()

df = pd.DataFrame({'x': [1, 2], 'y': [2, 3]})
df
_____()

st.write("bye")
_____()
