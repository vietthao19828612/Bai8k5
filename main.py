import streamlit as st
import pandas as pd
import google.generativeai as genai

# Đọc dữ liệu
df = pd.read_csv('bai8.csv')

st.title('Phan tich DL khach hang')

st.subheader('DL goc:')
st.dataframe(df)

# Phân tích
roi_bo = df[df['Diem tin dung'] <= 700]['ID KH'].tolist()

mua_hang = df[
    (df['Thu nhap'] >= 50000) & 
    (df['Diem tin dung'] >= 750)
]['ID KH'].tolist()

chi_tieu = df[
    df['Nghe'].isin(['Bac si','Chu doanh nghiep'])
]['ID KH'].tolist()

st.write('KH co kha nang roi bo:', roi_bo)
st.write('KH co kha nang mua hang thang toi:', mua_hang)
st.write('KH co kha nang chi tieu nhieu hon:', chi_tieu)

# AI phân tích
genai.configure(api_key=st.secrets['gg_api'])

model = genai.GenerativeModel('gemini-2.5-flash')

prompt = f"""
Đây là dữ liệu khách hàng:
{df.to_string()}

Hãy phân tích hành vi khách hàng và đưa ra insight quan trọng (200-300 từ)
"""

response = model.generate_content(prompt)

st.subheader('AI Insight:')
st.write(response.text)
