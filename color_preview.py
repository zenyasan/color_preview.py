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
