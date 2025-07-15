# ✅ Streamlit App: Dự đoán mức độ thiếu máu từ dữ liệu lâm sàng

import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# === Mô hình mẫu (có thể thay bằng mô hình thật đã huấn luyện và lưu bằng joblib) ===
def load_model():
    model = RandomForestClassifier()
    # Huấn luyện đơn giản với dữ liệu giả để chạy demo
    X_demo = [[25, 13.5, 85, 50], [60, 10.1, 70, 20], [30, 8.2, 60, 10], [50, 6.5, 55, 8]]
    y_demo = [0, 1, 2, 3]
    model.fit(X_demo, y_demo)
    return model

model = load_model()

# === Giao diện ứng dụng ===
st.set_page_config(page_title="Dự đoán Thiếu máu", layout="centered")
st.title("🔬 Dự đoán mức độ thiếu máu từ dữ liệu lâm sàng")
st.write("Nhập các chỉ số cơ bản để dự đoán mức độ thiếu máu theo chuẩn WHO.")

# === Nhập thông tin ===
age = st.slider("Tuổi", 1, 100, 30)
sex = st.selectbox("Giới tính", ["Nam", "Nữ"])
hb = st.number_input("Hemoglobin (g/dL)", 3.0, 20.0, 12.0)
mcv = st.number_input("MCV - Thể tích trung bình HC (fL)", 50.0, 120.0, 85.0)
ferritin = st.number_input("Ferritin (ng/mL)", 1.0, 500.0, 50.0)

# === Dự đoán ===
if st.button("Dự đoán"):
    input_data = np.array([[age, hb, mcv, ferritin]])
    prediction = model.predict(input_data)[0]

    # Giải thích mức độ thiếu máu
    levels = {
        0: ("Không thiếu máu", "🟢", "Bạn không có dấu hiệu thiếu máu."),
        1: ("Thiếu máu nhẹ", "🟡", "Theo dõi thêm chế độ ăn và tái kiểm tra định kỳ."),
        2: ("Thiếu máu vừa", "🟠", "Nên đi khám chuyên khoa huyết học để kiểm tra thêm."),
        3: ("Thiếu máu nặng", "🔴", "Cần được can thiệp y tế sớm, có thể cần điều trị đặc biệt.")
    }

    label, icon, message = levels.get(prediction, ("Không xác định", "⚪", "Không phân loại được."))

    st.markdown(f"## {icon} Kết quả: {label}")
    st.info(message)

# Footer
st.markdown("---")
st.caption("Demo App | Đề tài: Dự đoán mức độ thiếu máu từ dữ liệu lâm sàng | Khoa học dữ liệu y tế")
