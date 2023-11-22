import streamlit as st
from PIL import Image
st.title("Conversion App")

img =Image. open ("dollar.png")
st.sidebar.image (img)

curr =["Naira","Pounds","Dollars","Euros","Yen","Cedis"]
conv =[1, 1023, 816, 890, 114, 68]

def convert(num,initial,final):
    ini_id = curr.index(initial)
    fin_id = curr.index(final)

    value1 = conv[ini_id]
    value2 = conv[fin_id]

    result = num * value1 / value2

    return result

num = st. number_input ("How much are you converting")
initail= st.selectbox ("Amount currency",curr)
final =st.selectbox("Convertion currency",curr)

amount = convert (num,initail,final)

if st.button ("Convert"):
    st.write(amount)


