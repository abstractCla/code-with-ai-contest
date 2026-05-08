# 5G 信号可视化看板

## 项目简介

这是一个基于 Streamlit 框架开发的 5G 路测数据可视化看板，能够将枯燥的 5G 信号数据转化为高大上的交互式 Web 应用。

## 功能特性

### 基础功能
- **数据加载**：使用 pandas 库读取 CSV 数据，支持数据缓存
- **2D 散点地图**：使用 st.map() 展示信号分布，地图点根据 RSRP 强度着色
- **数据统计图表**：柱状图展示各频段基站数量和终端类型占比
- **RSRP-SINR 关系分析**：散点图展示信号质量与信噪比的关系

### 进阶功能
- **侧边栏联动筛选**：下拉菜单筛选频段（Band）和终端类型
- **范围滑动条**：RSRP 和 SINR 范围筛选器
- **实时更新**：所有筛选器联动更新地图和图表
- **3D 地图可视化**：使用 PyDeck HexagonLayer 展示信号热力图
- **关键指标卡片**：实时显示数据统计信息

## 快速开始

### 环境要求
- Python 3.8+
- 现代浏览器（Chrome、Firefox、Edge 等）

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行应用

```bash
streamlit run app.py
```

应用将在本地启动，默认访问地址：`http://localhost:8501`

## 项目结构

```
/workspace/
├── app.py                  # 主应用代码
├── requirements.txt         # 依赖包列表
├── README.md               # 项目说明文档
├── AI_PROMPTS.md           # AI 交互日志
├── screenshots/            # 运行截图（需手动添加）
│   └── README.md           # 截图添加说明
└── data/
    └── signal_samples.csv   # 5G 信号数据样本
```

## 数据字段说明

| 字段名 | 说明 | 示例值 |
|--------|------|--------|
| Latitude | 纬度坐标 | 31.209143 |
| Longitude | 经度坐标 | 121.482867 |
| CellID | 基站小区标识 | 1926 |
| Band | 频段 | n28, n41, n78 |
| RSRP_dBm | 参考信号接收功率 (dBm) | -94.94 |
| SINR_dB | 信噪比 (dB) | 5.44 |
| TerminalType | 终端类型 | Smartphone, CPE, IoT |
| Download_Mbps | 下载速率 (Mbps) | 138.21 |

## RSRP 信号质量标准

| RSRP 范围 | 信号质量 | 颜色标识 |
|-----------|----------|----------|
| > -90 dBm | 优秀 | 🟢 绿色 |
| -90 ~ -100 dBm | 良好 | 🟡 黄色 |
| -100 ~ -110 dBm | 一般 | 🟠 橙色 |
| < -110 dBm | 较差 | 🔴 红色 |

## 使用指南

### 筛选数据
1. 在左侧边栏选择频段（Band）
2. 选择终端类型
3. 调整 RSRP 和 SINR 范围滑动条
4. 所有可视化内容将实时更新

### 地图交互
- **2D 地图**：显示所有信号采样点，鼠标悬停可查看详细信息
- **3D 地图**：六边形高度代表下载速率，颜色深浅表示信号强度

### 查看统计数据
- 页面顶部显示关键指标卡片
- 中部展示数据统计图表
- 底部显示原始数据预览表格

## 运行截图

以下是 5G 信号可视化看板的运行截图，展示了应用的主要功能和交互界面：

### 截图列表

| 截图名称 | 文件路径 | 展示内容 |
|----------|----------|----------|
| 主页面与2D地图 | `screenshots/main_dashboard.png` | 标题、指标卡片、2D信号分布地图、侧边栏筛选器 |
| 3D地图与统计图表 | `screenshots/3d_map_charts.png` | 3D HexagonLayer 地图、频段分布柱状图、终端类型占比 |
| RSRP-SINR关系分析 | `screenshots/rsrp_sinr_scatter.png` | RSRP与SINR关系散点图、原始数据预览表格 |
| 频段筛选器 | `screenshots/band_filter.png` | 频段下拉菜单（n28/n41/n78）|
| 终端类型筛选器 | `screenshots/terminal_filter.png` | 终端类型下拉菜单（CPE/IoT/Smartphone）|

### 截图预览

#### 1. 主页面与2D地图

展示了应用的主界面，包含：
- 标题和欢迎信息
- 关键指标卡片（总数据点、平均RSRP、平均SINR、平均下载速率）
- 2D信号分布地图（根据RSRP着色）
- 左侧侧边栏筛选器

#### 2. 3D地图与统计图表

展示了：
- 3D HexagonLayer 可视化（高度随下载速率变化）
- 各频段基站数量分布柱状图
- 终端类型占比柱状图

#### 3. RSRP-SINR关系分析

展示了：
- RSRP与SINR关系散点图
- 原始数据预览表格（前20行）

#### 4. 筛选器交互

展示了侧边栏的筛选功能：
- 频段选择（n28、n41、n78）
- 终端类型选择（CPE、IoT、Smartphone）
- RSRP范围滑动条
- SINR范围滑动条

### 截图存放位置

所有截图均存放在 `screenshots/` 目录下，供评审参考。

## 技术栈

- **Web 框架**：Streamlit
- **数据处理**：Pandas、NumPy
- **地图可视化**：st.map()、PyDeck
- **图表**：st.bar_chart()、st.scatter_chart()
- **交互组件**：st.selectbox()、st.slider()、st.metric()

## 开发说明

本项目通过 AI Coding Agent 辅助开发，完整的 AI 交互记录请参见 `AI_PROMPTS.md` 文件。

### 使用 AI 工具开发的优势
1. **快速原型**：AI 可以快速生成基础代码框架
2. **问题解答**：遇到问题时 AI 可以提供解决方案
3. **代码优化**：AI 可以帮助优化和重构代码
4. **文档生成**：AI 可以生成规范的注释和说明文档

## 竞赛信息

本项目是为 **"Code with AI" 海选赛：5G 信号可视化看板挑战** 开发的作品。

### 验收标准

#### 基础关卡（必做，完赛基准线）
- ✅ **数据加载**：使用 pandas 库读取 CSV 数据
- ✅ **信号散点地图**：2D 地图显示信号分布，地图点根据 RSRP_dBm 变色
  - RSRP > -90 dBm 为绿色
  - RSRP < -110 dBm 为红色
- ✅ **数据概览图表**：柱状图统计各频段基站数量和终端类型占比

#### 进阶关卡（加分项）
- ✅ **侧边栏联动筛选**：下拉菜单筛选频段、滑动条筛选 RSRP 范围
- ✅ **实时更新**：筛选器拖动时地图和图表实时更新
- ✅ **3D 地图**：pydeck HexagonLayer，六边形"站起来"高度随下载速率变化
- ✅ **工程化素养**：代码规范注释

### 提交方式
```bash
# 基础关卡完成
git tag basic-done
git push origin basic-done

# 进阶关卡完成
git tag advanced-done
git push origin advanced-done
```

### 硬核交付物清单
1. ✅ **源代码**：app.py + requirements.txt
2. ✅ **项目说明文档**：README.md
3. ⚠️ **运行截图**：screenshots/ 目录（需手动添加）
4. ✅ **Agent 交互日志**：AI_PROMPTS.md

## 许可证

本项目仅供学习和竞赛使用。

## 联系方式

如有问题或建议，请通过 GitHub Issues 联系我们。
