import streamlit as st

st.set_page_config(page_title="カラーパレット", page_icon="🎨", layout="wide")

st.title("🎨 強めグラデーション - 青系カラーパレット")
st.markdown("### グラデーションを強調した青系デザイン")

color_schemes = {
    "案1：ディープブルーグラデーション（濃淡強め）": {
        "primary": "#0066ff",
        "secondary": "#0033cc",
        "accent": "#6600ff",
        "bg_from": "#0a0e27",
        "bg_to": "#1a1d3a",
        "description": "濃い青から明るい青への強いグラデーション"
    },
    "案2：エレクトリックブルーグラデーション（鮮やか）": {
        "primary": "#0080ff",
        "secondary": "#0040ff",
        "accent": "#8000ff",
        "bg_from": "#0a0e27",
        "bg_to": "#1a1d3a",
        "description": "鮮やかな青のコントラストが強いグラデーション"
    },
    "案3：ネオンブルーグラデーション（最も強い）": {
        "primary": "#00aaff",
        "secondary": "#0055ff",
        "accent": "#aa00ff",
        "bg_from": "#0a0e27",
        "bg_to": "#1a1d3a",
        "description": "明るい青から濃い青への最も強いグラデーション"
    },
    "案4：サファイアブルーグラデーション（高級感）": {
        "primary": "#0077ff",
        "secondary": "#003dff",
        "accent": "#7700ff",
        "bg_from": "#0a0e27",
        "bg_to": "#1a1d3a",
        "description": "サファイアのような深い青のグラデーション"
    },
    "案5：オーシャンブルーグラデーション（深海）": {
        "primary": "#0099ff",
        "secondary": "#0044ff",
        "accent": "#9900ff",
        "bg_from": "#0a0e27",
        "bg_to": "#1a1d3a",
        "description": "海の深さを表現した青のグラデーション"
    }
}

for scheme_name, colors in color_schemes.items():
    st.markdown(f"## {scheme_name}")
    st.caption(colors['description'])
    
    cols = st.columns(5)
    
    with cols[0]:
        st.markdown(f"""
        <div style="
            background: {colors['primary']};
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            color: white;
            font-weight: bold;
            font-size: 14px;
            box-shadow: 0 0 30px {colors['primary']}80;
        ">
            メインカラー<br>{colors['primary']}
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown(f"""
        <div style="
            background: {colors['secondary']};
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            color: white;
            font-weight: bold;
            font-size: 14px;
            box-shadow: 0 0 30px {colors['secondary']}80;
        ">
            セカンダリ<br>{colors['secondary']}
        </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown(f"""
        <div style="
            background: {colors['accent']};
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            color: white;
            font-weight: bold;
            font-size: 14px;
            box-shadow: 0 0 30px {colors['accent']}80;
        ">
            アクセント<br>{colors['accent']}
        </div>
        """, unsafe_allow_html=True)
    
    with cols[3]:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            color: white;
            font-weight: bold;
            font-size: 14px;
            box-shadow: 0 0 30px {colors['primary']}60;
        ">
            グラデーション<br>強め
        </div>
        """, unsafe_allow_html=True)
    
    with cols[4]:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {colors['primary']}, {colors['accent']});
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            color: white;
            font-weight: bold;
            font-size: 14px;
            box-shadow: 0 0 30px {colors['accent']}60;
        ">
            3色混合<br>グラデーション
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']}, {colors['accent']});
        padding: 60px;
        border-radius: 25px;
        text-align: center;
        color: white;
        font-size: 2rem;
        font-weight: bold;
        margin: 20px 0;
        box-shadow: 0 0 50px {colors['primary']}80;
    ">
        3色グラデーション - 強調表示
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {colors['primary']}30, {colors['secondary']}30);
            backdrop-filter: blur(10px);
            border: 2px solid {colors['primary']};
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 8px 32px {colors['primary']}50, 0 0 40px {colors['primary']}40;
        ">
            <h3 style="color: {colors['primary']}; margin: 0; text-shadow: 0 0 20px {colors['primary']};">💰 現在価格</h3>
            <h1 style="
                background: linear-gradient(90deg, {colors['primary']}, {colors['secondary']});
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin: 10px 0;
                font-size: 2.5rem;
            ">$5,108.50</h1>
            <p style="color: {colors['secondary']}; text-shadow: 0 0 10px {colors['secondary']};">+25.30 (+0.49%)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {colors['secondary']}30, {colors['accent']}30);
            backdrop-filter: blur(10px);
            border: 2px solid {colors['secondary']};
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 8px 32px {colors['secondary']}50, 0 0 40px {colors['accent']}40;
        ">
            <h3 style="color: {colors['secondary']}; margin: 0; text-shadow: 0 0 20px {colors['secondary']};">📈 RSI</h3>
            <h1 style="
                background: linear-gradient(90deg, {colors['secondary']}, {colors['accent']});
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin: 10px 0;
                font-size: 2.5rem;
            ">62.5</h1>
            <p style="color: {colors['accent']}; text-shadow: 0 0 10px {colors['accent']};">中立</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin: 30px 0;">
        <button style="
            background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
            color: white;
            border: 2px solid white;
            padding: 15px 40px;
            border-radius: 15px;
            font-weight: bold;
            font-size: 1.2rem;
            cursor: pointer;
            box-shadow: 0 0 40px {colors['primary']}80, 0 0 60px {colors['secondary']}60;
        ">🔄 更新ボタン</button>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="
        display: flex;
        gap: 10px;
        background: rgba(10,14,39,0.8);
        padding: 10px;
        border-radius: 15px;
        border: 1px solid {colors['primary']}50;
    ">
        <div style="
            background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
            padding: 15px 30px;
            border-radius: 12px;
            color: white;
            font-weight: bold;
            box-shadow: 0 0 30px {colors['primary']}80;
        ">📊 選択中</div>
        <div style="
            background: linear-gradient(135deg, {colors['primary']}20, {colors['secondary']}20);
            padding: 15px 30px;
            border-radius: 12px;
            color: {colors['primary']};
            font-weight: bold;
            border: 1px solid {colors['primary']}50;
        ">💨 スキャル</div>
        <div style="
            background: linear-gradient(135deg, {colors['primary']}20, {colors['secondary']}20);
            padding: 15px 30px;
            border-radius: 12px;
            color: {colors['primary']};
            font-weight: bold;
            border: 1px solid {colors['primary']}50;
        ">📈 デイトレ</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("## 🎯 選び方のヒント")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **案1-2: 濃淡強め**
    - コントラストが強い
    - 読みやすい
    - 長時間使用向き
    """)

with col2:
    st.info("""
    **案3: 最も鮮やか**
    - 最も目を引く
    - ゲーマー向け
    - インパクト重視
    """)

with col3:
    st.info("""
    **案4-5: バランス型**
    - 高級感がある
    - 落ち着いている
    - プロトレーダー向け
    """)

st.success("### ✅ 気に入った案の番号（1〜5）を教えてください！")
st.info("または、「もっと明るく」「もっと濃く」などの調整リクエストもOKです！")
