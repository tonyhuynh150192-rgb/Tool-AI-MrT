import streamlit as st

st.set_page_config(
    page_title="Tool AI Mr.T",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 TOOL AI MR.T")

st.subheader("AI Auto Key Detection")

st.write(
    "Công cụ AI tự động phân tích Tone/Key của nhạc "
    "và hỗ trợ thiết lập Auto-Tune."
)

uploaded_file = st.file_uploader(
    "Chọn file nhạc",
    type=["mp3", "wav", "m4a", "flac"]
)

if uploaded_file is not None:
    st.success(f"Đã nhận file: {uploaded_file.name}")

    st.audio(uploaded_file)

    st.info(
        "Module AI dò Key sẽ được tích hợp ở bước tiếp theo."
    )
