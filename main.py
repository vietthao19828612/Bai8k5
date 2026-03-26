csv_data = '''ID KH,Tuoi,gioi tinh,Thu nhap,Nghe,Diem tin dung,SP da mua,Gia,So luong,ngay mua
1,30,50000,ky su phan mem , 750,Dien thoai,500,1,2026-02-15
2,25,Nu,30000,Giao vien,680,may tinh,700,1,2026-02-10
3.40,Nam,75000,Bac si,820,Tivi,1000,1,2026-03-02
4,50,Nu,40000,chu doanh nghiep,700,Tu lanh,1200,2,2026-01-28
5,60,Nam,60000,Nghi huu,800,May giat,1500,1,2026-01-30
'''
with open('bai8.csv','w',encoding='utf-8') as f: f.write(csv_data)
import streamlit as st, pandas as pd
df = pd.read_csv('bai8.csv')
st.title('Phan tich DL khach hang')
st.subheader('Dl goc:')
st.dataframe(df)
roi_bo = df[df['Diem tin dung'] <= 700]['ID KH'].tolist()
mua_hang = df[(df['Thu nhap'] >= 50000) & (df['Diem tin dung'] >= 750)]['ID KH'].tolist()
chi_tieu = df[df['Nghe'].isin(['Bac si','Chu doanh nghiep'])]['ID KH'].tolist()
st.write('KH co kha nang roi bo:', roi_bo)
st.write('KH co kha nang mua hang thang toi', mua_hang)
st.write('KH co kha nang chi tieu nhieu hon',chi_tieu)
import google.generativeai as genai
genai.configure(api_key=st.secrets['gg_api'])
model = genai.GenrativeModel('gemini-2.5-flash')
p = f"""Đây là dữ liệu khách hàng: {df.to_string()}.
Hãy phân tích hành vi khách hàng và đưa ra insight quan trọng (200-300 từ)
"""
r = model.generate_content(p)
st.subheader("Phân tích từ AI (Gemini):")
st.write(r.text)
