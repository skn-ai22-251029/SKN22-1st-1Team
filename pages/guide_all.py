import streamlit as st

st.set_page_config(page_title="긴급 연락처", page_icon="📞", layout="wide")

# -----------------------------
# 상단: 메인페이지 버튼
# -----------------------------
top_cols = st.columns([1, 3])
with top_cols[0]:
    if st.button("🏠 메인페이지"):
        st.switch_page("safe_drive_app.py")   # 메인페이지로 이동

# -----------------------------
# 타이틀 및 설명 (CSS 적용)
# -----------------------------
style = """
    <style>
    /* 사이드바 숨김 */
    section[data-testid="stSidebar"] {
        display: none;
    }
    /* 상단 메뉴(Deploy 등) 숨김 */
    header {
        visibility: hidden;
    }

    .title-center {
        text-align: center;
        font-size: 3em;   /* 타이틀 크게 */
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    .subtitle-center {
        text-align: center;
        font-size: 1.5em; /* 설명 크게 */
        color: #444444;
        margin-bottom: 20px;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 25px;
        border-radius: 12px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.15);
        margin: 10px;
        text-align: center;
    }
    .card h3 {
        margin-top: 0;
        color: #333333;
        font-size: 1.6em;
    }
    .card p {
        font-size: 1.3em;
        font-weight: bold;
        color: #004080;
    }
    </style>
"""
st.markdown(style, unsafe_allow_html=True)

st.markdown('<div class="title-center">안전운전 가이드</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-center">원하시는 메뉴를 선택하세요.</div>', unsafe_allow_html=True)

st.divider()

# -----------------------------
# 메뉴 1행 4열 카드 (각 카드 클릭 시 페이지 이동)
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card"><h3>📊 교통사고 분석</h3><p>2가지 옵션<br>선택에 따른 분석 결과</p></div>', unsafe_allow_html=True)
    if st.button("➡️ 이동", key="btn1"):
        st.switch_page("pages/driver_input.py")

with col2:
    st.markdown('<div class="card"><h3>☑️ 운전 체크리스트</h3><p>안전운전<br>셀프 체크</p></div>', unsafe_allow_html=True)
    if st.button("➡️ 이동", key="btn2"):
        st.switch_page("pages/driver_checklist.py")

with col3:
    st.markdown('<div class="card"><h3>🚗 안전운전 팁</h3><p>안전운전<br>꿀팁 안내</p></div>', unsafe_allow_html=True)
    if st.button("➡️ 이동", key="btn3"):
        st.switch_page("pages/safe_drive_tip.py")

with col4:
    st.markdown('<div class="card"><h3>📞 긴급연락</h3><p>행동요령<br>교통사고 신고 및 처리</p></div>', unsafe_allow_html=True)
    if st.button("➡️ 이동", key="btn4"):
        st.switch_page("pages/EC_details.py")

st.divider()

# -----------------------------
# 하단 좌측: 이전페이지 버튼
# -----------------------------
bottom_cols = st.columns([1, 1, 1, 1, 1])
with bottom_cols[0]:
    if st.button("⬅️ 이전페이지"):
        st.switch_page("driver_checklist.py")   # 로컬 이전페이지로 이동