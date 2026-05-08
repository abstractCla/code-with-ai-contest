import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(page_title="5G 信号可视化看板", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('data/signal_samples.csv')
    return df

def get_signal_color(rsrp):
    if rsrp > -90:
        return '#228B22'
    elif rsrp > -100:
        return '#FFD700'
    elif rsrp > -110:
        return '#FF8C00'
    else:
        return '#DC143C'

df = load_data()

st.title("📡 5G 信号可视化看板")
st.markdown("欢迎来到 **'Code with AI' 极客探索赛** 5G 信号分析系统！")

st.sidebar.header("🔍 数据筛选")
st.sidebar.markdown("使用下方筛选器实时过滤数据")

band_options = ['全部'] + sorted(df['Band'].unique().tolist())
selected_band = st.sidebar.selectbox("选择频段 (Band)", band_options)

terminal_options = ['全部'] + sorted(df['TerminalType'].unique().tolist())
selected_terminal = st.sidebar.selectbox("选择终端类型", terminal_options)

rsrp_min, rsrp_max = st.sidebar.slider(
    "RSRP 范围 (dBm)",
    float(df['RSRP_dBm'].min()),
    float(df['RSRP_dBm'].max()),
    (float(df['RSRP_dBm'].min()), float(df['RSRP_dBm'].max()))
)

sinr_min, sinr_max = st.sidebar.slider(
    "SINR 范围 (dB)",
    float(df['SINR_dB'].min()),
    float(df['SINR_dB'].max()),
    (float(df['SINR_dB'].min()), float(df['SINR_dB'].max()))
)

filtered_df = df[
    (df['RSRP_dBm'] >= rsrp_min) & (df['RSRP_dBm'] <= rsrp_max) &
    (df['SINR_dB'] >= sinr_min) & (df['SINR_dB'] <= sinr_max)
]

if selected_band != '全部':
    filtered_df = filtered_df[filtered_df['Band'] == selected_band]

if selected_terminal != '全部':
    filtered_df = filtered_df[filtered_df['TerminalType'] == selected_terminal]

filtered_df['color'] = filtered_df['RSRP_dBm'].apply(get_signal_color)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("总数据点", len(filtered_df))

with col2:
    avg_rsrp = filtered_df['RSRP_dBm'].mean()
    st.metric("平均 RSRP", f"{avg_rsrp:.2f} dBm")

with col3:
    avg_sinr = filtered_df['SINR_dB'].mean()
    st.metric("平均 SINR", f"{avg_sinr:.2f} dB")

with col4:
    avg_speed = filtered_df['Download_Mbps'].mean()
    st.metric("平均下载速率", f"{avg_speed:.2f} Mbps")

st.subheader("📍 信号分布地图 (2D)")
st.map(filtered_df, latitude='Latitude', longitude='Longitude', color='color',
       size=50, zoom=12)

st.subheader("🗺️ 信号分布地图 (3D)")
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v11',
    initial_view_state=pdk.ViewState(
        latitude=filtered_df['Latitude'].mean(),
        longitude=filtered_df['Longitude'].mean(),
        zoom=12,
        pitch=45
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=filtered_df,
            get_position='[Longitude, Latitude]',
            get_weight='Download_Mbps',
            radius=100,
            elevation_scale=50,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            color_range=[[0, 230, 0], [255, 215, 0], [255, 69, 0], [255, 0, 0]],
            get_fill_color='[RSRP_dBm + 130, 200, RSRP_dBm + 130, 200]'
        )
    ],
    tooltip={
        'html': '<b>RSRP:</b> {RSRP_dBm} dBm<br/><b>SINR:</b> {SINR_dB} dB<br/><b>下载速率:</b> {Download_Mbps} Mbps',
        'style': {'backgroundColor': 'steelblue', 'color': 'white'}
    }
))

st.subheader("📊 数据统计分析")

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.markdown("**各频段基站数量分布**")
    band_counts = filtered_df['Band'].value_counts()
    st.bar_chart(band_counts)
    st.caption(f"共计 {len(band_counts)} 个频段")

with col_chart2:
    st.markdown("**终端类型占比**")
    terminal_counts = filtered_df['TerminalType'].value_counts()
    st.bar_chart(terminal_counts)
    st.caption(f"共计 {len(terminal_counts)} 种终端类型")

st.subheader("📈 RSRP 与 SINR 关系分析")
chart_data = filtered_df[['RSRP_dBm', 'SINR_dB', 'Download_Mbps']].copy()
st.scatter_chart(chart_data, x='RSRP_dBm', y='SINR_dB')

st.subheader("📋 原始数据预览")
st.dataframe(filtered_df.head(20), use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📌 图例说明")
st.sidebar.markdown("""
- **RSRP > -90 dBm**: 🟢 优秀信号
- **RSRP -90 ~ -100 dBm**: 🟡 良好信号
- **RSRP -100 ~ -110 dBm**: 🟠 一般信号
- **RSRP < -110 dBm**: 🔴 较差信号
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 数据字段说明")
st.sidebar.markdown("""
- **Latitude/Longitude**: 经纬度坐标
- **CellID**: 基站小区ID
- **Band**: 频段 (n28/n41/n78)
- **RSRP_dBm**: 参考信号接收功率
- **SINR_dB**: 信噪比
- **TerminalType**: 终端类型
- **Download_Mbps**: 下载速率 (Mbps)
""")

st.markdown("---")
st.markdown("© 2025 Code with AI 挑战赛 | 5G 信号可视化看板")
