import streamlit as st
import pandas as pd

# Tạo file CSV
csv_data = '''ID KH,Tuoi,gioi tinh,Thu nhap,Nghe,Diem tin dung,SP da mua,Gia,So luong,ngay mua
1,30,Nam,50000,Ky su phan mem,750,Dien thoai,500,1,2026-02-15
2,25,Nu,30000,Giao vien,680,May tinh,700,1,2026-02-10
3,40,Nam,75000,Bac si,820,Tivi,1000,1,2026-03-02
4,50,Nu,40000,Chu doanh nghiep,700,Tu lanh,1200,2,2026-01-28
5,60,Nam,60000,Nghi huu,800,May giat,1500,1,2026-01-30
'''

with open('bai8.csv','w',encoding='utf-8') as f:
    f.write(csv_data)

# Đọc dữ liệu
df = pd.read_csv('bai8.csv')

# Làm sạch dữ liệu
df.columns = df.columns.str.strip()

# Ép kiểu số
df['Diem tin dung'] = pd.to_numeric(df['Diem tin dung'])
df['Thu nhap'] = pd.to_numeric(df['Thu nhap'])

# Giao diện
st.title('Phan tich DL khach hang')

st.subheader('Du lieu goc:')
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

# Hiển thị
st.write('KH co kha nang roi bo:', roi_bo)
st.write('KH co kha nang mua hang thang toi:', mua_hang)
st.write('KH co kha nang chi tieu nhieu hon:', chi_tieu)
