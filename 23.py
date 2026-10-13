import streamlit as st
import random

# 페이지 기본 설정 (제목 및 아이콘)
st.set_page_config(page_title="알록달록 로또 번호 생성기", page_icon="🍀")


# 로또 번호 범위에 따른 공 색상 스타일 반환 함수
def get_ball_style(number):
    # 구간별 공식 색상 지정 (배경색, 글자색)
    if 1 <= number <= 10:
        bg, fg = "#fbc400", "black"  # 노란색
    elif 11 <= number <= 20:
        bg, fg = "#69c8f2", "black"  # 파란색
    elif 21 <= number <= 30:
        bg, fg = "#ff7272", "white"  # 빨간색
    elif 31 <= number <= 40:
        bg, fg = "#aaaaaa", "black"  # 회색
    else:
        bg, fg = "#b0d840", "black"  # 초록색

    # HTML을 이용해 동그란 공 모양(원형)과 색상 지정
    return f"background-color: {bg}; color: {fg}; border-radius: 50%; width: 36px; height: 36px; display: inline-flex; align-items: center; justify-content: center; font-weight: bold; margin: 3px; font-size: 14px;"


# --- 웹 화면 구성 ---
st.title("🍀 알록달록 로또 번호 생성기")
st.write("버튼을 누르면 1부터 45 사이의 번호 6개로 구성된 **5세트**의 행운의 번호가 나타납니다!")

# 번호 생성 버튼
if st.button("번호 생성하기", type="primary"):
    st.markdown("---")
    st.subheader("✨ 추천 로또 번호 5세트")

    # 최대 5세트 반복 생성
    for i in range(5):
        # 1부터 45 사이의 숫자 중 중복 없이 6개 추출 후 오름차순 정렬
        lotto_nums = sorted(random.sample(range(1, 46), 6))

        # 세트 레이블과 공 모양 HTML 조합
        row_html = f"<div style='margin-bottom: 12px; display: flex; align-items: center;'>"
        row_html += f"<span style='font-weight: bold; margin-right: 12px; font-size: 16px;'>{i + 1}세트:</span>"

        # 6개의 숫자를 각각 알록달록한 공 모양으로 변환
        for num in lotto_nums:
            style = get_ball_style(num)
            row_html += f"<span style='{style}'>{num:02d}</span>"

        row_html += "</div>"

        # Streamlit에서 HTML 렌더링 (공 모양 스타일 적용을 위해 unsafe_allow_html=True 사용)
        st.markdown(row_html, unsafe_allow_html=True)
