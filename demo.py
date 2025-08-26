# demo.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 页面设置
st.set_page_config(page_title="商参星盘", page_icon="📊", layout="wide")

# 使用美团配色
primary_color = '#FFD000'  # 美团黄
secondary_color = '#FFE580'
background_color = '#F5F5F5'

# 侧边栏 - 店铺选择
with st.sidebar:
    st.header("📊 商参星盘")
    shop_options = ['朝阳区望京奶茶店 (默认)', '海淀区中关村咖啡厅', '丰台区小吃店']
    selected_shop = st.selectbox("选择诊断店铺", shop_options)
    st.info(f"已选择: **{selected_shop}**")
    st.divider()
    if st.button("🔄 一键生成诊断报告", use_container_width=True):
        st.success("报告已刷新!")
    st.caption("数据更新至: 2024-05-20 12:00")

# 主页面布局
st.title("商参星盘 - 店铺经营诊断中心")

# 1. 总览 - 五维雷达图
st.header("📈 总览")
col1, col2 = st.columns([2, 1])

with col1:
    # 创建雷达图
    categories = ['店铺营收', '流量转化', '履约时效', '库存周转', '服务分析']
    shop_scores = [85, 70, 60, 75, 65]  # 本店得分
    area_avg_scores = [70, 75, 80, 70, 75]  # 商圈均值

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=shop_scores + [shop_scores[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name='本店表现',
        line=dict(color=primary_color)
    ))
    fig.add_trace(go.Scatterpolar(
        r=area_avg_scores + [area_avg_scores[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name='商圈均值',
        line=dict(color='lightgray')
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.metric("综合健康度", "72分", "↑2分", delta_color="normal")
    st.progress(0.72, "优于56%同行")
    st.write("**诊断摘要:**")
    st.write("• 🟢 营收表现优秀")
    st.write("• 🟡 流量转化待提升")
    st.write("• 🔴 履约时效需优化")

# 2. 店铺营收模块
st.header("💰 店铺营收")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("当日收入", "¥8,542", "+12%", delta_color="inverse")
with col2:
    st.metric("有效订单", "236单", "+8%")
with col3:
    st.metric("营业额", "¥12,845", "+15%")
with col4:
    st.metric("支出", "¥4,302", "+5%", delta_color="inverse")

# 3. 流量转化分析
st.header("🌐 流量转化")

# 漏斗图数据
funnel_data = pd.DataFrame({
    '阶段': ['曝光', '进店', '下单'],
    '人数': [750, 330, 109],
    '转化率': ['100%', '44.0%', '33.0%']
})

col1, col2 = st.columns([2, 1])
with col1:
    fig = px.funnel(funnel_data, x='人数', y='阶段',
                   title='流量转化漏斗', color_discrete_sequence=[primary_color])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write("**诊断建议:**")
    st.warning("店铺近30日曝光人数较上月同期下降6.8%")
    if st.button("✅ 去开通一站式推广", use_container_width=True):
        st.success("已为您开启流量推广服务!")

# 4. 客群分析
st.header("👥 客群分析")

tab1, tab2 = st.tabs(["新老客分析", "会员分析"])
with tab1:
    fig = px.pie(values=[189, 128], names=['老客', '新客'],
                title='新老客占比', color_discrete_sequence=[primary_color, secondary_color])
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    member_data = pd.DataFrame({
        '等级': ['黑钻会员', '铂金会员', '黄金会员', '普通会员'],
        '人数': [150, 134, 189, 100]
    })
    fig = px.bar(member_data, x='等级', y='人数',
                title='会员等级分布', color_discrete_sequence=[primary_color])
    st.plotly_chart(fig, use_container_width=True)

# 5. 履约时效分析
st.header("⏱ 履约时效")

# 出餐率时序数据
time_data = pd.DataFrame({
    '时段': ['8-10点', '10-13点', '13-18点', '18-20点', '20-22点'],
    '本店出餐率': [85, 42, 75, 65, 60],
    '商圈均值': [88, 65, 80, 70, 68]
})

fig = px.line(time_data, x='时段', y=['本店出餐率', '商圈均值'],
             title='分时段出餐率对比',
             color_discrete_sequence=[primary_color, 'gray'])
st.plotly_chart(fig, use_container_width=True)

st.write("**诊断建议:**")
st.error("高峰时段(10-13点)出餐率42%低于商圈均值65%")
st.button("📋 查看备餐优化方案", key="fulfillment_btn")

# 6. 服务分析
st.header("⭐ 服务分析")

# 差评原因分析
complaint_data = pd.DataFrame({
    '原因': ['配送慢', '口味差', '包装破损', '服务态度', '其他'],
    '数量': [45, 30, 15, 8, 2]
})

fig = px.bar(complaint_data, x='原因', y='数量',
            title='差评原因分析', color_discrete_sequence=[primary_color])
st.plotly_chart(fig, use_container_width=True)

# 底部诊断总结
st.divider()
st.subheader("📋 综合诊断建议")
st.write("""
1. **营收表现优秀**：继续保持当前营收增长势头，建议扩大优势
2. **流量转化不足**：曝光量下降明显，建议开通平台推广服务
3. **履约时效待优化**：重点改善高峰时段出餐效率，建议参考备餐优化方案
4. **服务质量稳定**：差评率处于行业较低水平，继续保持
""")

if st.button("🖨 生成完整诊断报告", use_container_width=True, type="primary"):
    st.balloons()
    st.success("✅ 诊断报告已生成完毕！可下载分享给运营团队")