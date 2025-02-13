import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

# ฟังก์ชันคำนวณพิกัดหัวใจ
def hearta(k):
    return 15 * np.sin(k)**3

def heartb(k):
    return 12 * np.cos(k) - 5 * np.cos(2*k) - 2 * np.cos(3*k) - np.cos(4*k)

# ส่วนแสดงผลเว็บ
st.title("💖 Valentine's Envelope 💌")
st.write("คลิกปุ่มด้านล่างเพื่อแสดงหัวใจ!")

if st.button("เปิดซองจดหมาย"):
    # คำนวณจุดหัวใจ
    k = np.linspace(0, 2 * np.pi, 600)
    x = hearta(k)
    y = heartb(k)

    # วาดหัวใจ
    fig, ax = plt.subplots()
    ax.plot(x, y, "r", linewidth=2)
    ax.fill(x, y, "red", alpha=0.5)
    ax.set_aspect("equal")
    ax.axis("off")

    st.pyplot(fig)
