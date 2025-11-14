import streamlit as st
import base64
import os

# 페이지 설정: 사이드바 기본 숨김
st.set_page_config(
    page_title="안전한 운전, 사고 없는 내일",
    layout="wide",
    initial_sidebar_state="collapsed"   # 사이드바 접기
)

# 이미지 Base64 변환 함수
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 현재 파일 위치 기준 이미지 경로
current_dir = os.path.dirname(__file__)
img_path = os.path.join("web_design/", "safecar1.png")   # 배경 이미지 파일
img_base64 = get_base64_of_bin_file(img_path)

# CSS 정의 (사이드바, 상단 메뉴 숨김 포함)
st.markdown(
    f"""
    <style>
    /* 배경 이미지 */
    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
    }}
    /* 메인 박스 */
    .main-box {{
        background: rgba(255,255,255,0.85);
        padding: 40px;
        border-radius: 20px;
        max-width: 950px;
        margin:auto;
        margin-top: 40px;
        margin-bottom: 60px;
        text-align: center; /* 내부 콘텐츠 중앙 정렬 */
    }}
    .main-title {{
        font-size: 54px; 
        font-weight: 900; 
        color: #222; 
        line-height: 1.1; 
        margin-bottom: 0px;
    }}
    .sub-title {{
        font-size: 50px; 
        font-weight: 700; 
        color: #428AF7; 
        margin-bottom: 32px; 
        margin-top: -10px;
    }}
    .desc {{
        font-size: 22px; 
        color: #444; 
        margin-bottom: 40px;
    }}
    /* 버튼 스타일 */
    div.stElementContainer.element-container.st-key-guide_btn {{
        margin:auto; /* 버튼 자체 중앙 정렬 */
    }}
    div.stButton > button:first-child {{
        background:#7B3FE4; /* 보라색 버튼 */
        color:white;
        borde   r:none;
        border-radius:8px;
        padding:16px 28px;
        font-size:18px;
        font-weight:600;
        cursor:pointer;
        
        display:block;
    }}
    div.stButton {{
        text-align: center; /* 버튼 컨테이너 중앙 정렬 */
    }}
    /* 사이드바 완전 숨김 */
    section[data-testid="stSidebar"] {{
        display: none;
    }}
    /* 상단 메뉴(Deploy 등) 숨김 */
    header {{
        visibility: hidden;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 메인 박스 + 타이틀 + 문구 + 버튼
with st.container():
    st.markdown(
        """
        <div class="main-box">
            <div class="main-title">안전한 운전,</div>
            <div class="sub-title">사고 없는 내일</div>
            <div class="desc">
                안전 운전 팁과 교통사고 통계로<br>
                당신의 안전한 운전을 지켜드립니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 버튼을 메인 박스 안쪽 설명 바로 아래 중앙에 배치
    if st.button("안전 가이드 시작하기 →", key="guide_btn"):
        st.switch_page("pages/guide_all.py")
