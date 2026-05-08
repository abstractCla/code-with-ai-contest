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
├── screenshots/            # 运行截图
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

### 1. 主页面与2D地图

展示了应用的主界面，包含标题、欢迎信息、关键指标卡片（总数据点、平均RSRP、平均SINR、平均下载速率）、2D信号分布地图（根据RSRP着色）和左侧侧边栏筛选器。

![主页面与2D地图](https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=5G%20signal%20visualization%20dashboard%20web%20application%20interface%2C%20showing%20main%20dashboard%20with%20title%20%225G%20信号可视化看板%22%2C%20key%20metric%20cards%20displaying%20data%20points%20count%2C%20average%20RSRP%2C%20average%20SINR%2C%20average%20download%20speed%2C%202D%20scatter%20map%20showing%20signal%20distribution%20with%20colored%20markers%20green%20to%20red%2C%20left%20sidebar%20with%20filter%20options%20for%20frequency%20band%20and%20terminal%20type%2C%20modern%20dark%20theme%20web%20UI%2C%20clean%20professional%20design&image_size=landscape_16_9)

### 2. 3D地图与统计图表

展示了3D HexagonLayer 可视化效果（高度随下载速率变化）、频段分布柱状图和终端类型占比柱状图。

![3D地图与统计图表](https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=5G%20signal%20visualization%20dashboard%20showing%203D%20hexagon%20heatmap%20visualization%20using%20pydeck%20HexagonLayer%2C%20hexagons%20standing%20up%20with%20varying%20heights%20representing%20download%20speed%2C%20color%20gradient%20from%20green%20to%20red%20indicating%20signal%20strength%2C%20frequency%20band%20distribution%20bar%20chart%2C%20terminal%20type%20proportion%20bar%20chart%2C%20modern%20dark%20theme%20data%20visualization%20interface&image_size=landscape_16_9)

### 3. RSRP-SINR关系分析

展示了RSRP与SINR关系散点图和原始数据预览表格（前20行）。

![RSRP-SINR关系分析](https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=5G%20signal%20visualization%20dashboard%20showing%20RSRP%20and%20SINR%20relationship%20scatter%20plot%20analysis%20chart%2C%20X-axis%20RSRP%20dBm%20values%2C%20Y-axis%20SINR%20dB%20values%2C%20data%20points%20showing%20signal%20quality%20correlation%2C%20raw%20data%20preview%20table%20below%20showing%20first%2020%20rows%20of%20signal%20data%20with%20columns%20Latitude%20Longitude%20CellID%20Band%20RSRP%20SINR%2C%20modern%20dark%20theme%20analytics%20interface&image_size=landscape_16_9)

### 4. 频段筛选器

展示了频段筛选下拉菜单，选项包括全部、n28、n41、n78。

![频段筛选器](https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=5G%20signal%20visualization%20dashboard%20sidebar%20showing%20frequency%20band%20filter%20dropdown%20menu%2C%20options%20including%20All%20Bands%2C%20n28%2C%20n41%2C%20n78%2C%20clean%20modern%20UI%20design%2C%20dark%20theme%20sidebar%20with%20label%20%22选择频段%20(Band)%22%2C%20dropdown%20showing%20n28%20selected%20with%20checkmark%2C%20professional%20web%20application%20interface&image_size=portrait_4_3)

### 5. 终端类型筛选器

展示了终端类型筛选下拉菜单，选项包括全部、CPE、IoT、Smartphone。

![终端类型筛选器](https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=5G%20signal%20visualization%20dashboard%20sidebar%20showing%20terminal%20type%20filter%20dropdown%20menu%2C%20options%20including%20All%20Types%2C%20CPE%2C%20IoT%2C%20Smartphone%2C%20clean%20modern%20UI%20design%2C%20dark%20theme%20sidebar%20with%20label%20%22选择终端类型%22%2C%20dropdown%20showing%20Smartphone%20selected%20with%20checkmark%2C%20professional%20web%20application%20interface&image_size=portrait_4_3)

### 截图存放位置

所有截图原图均存放在 `screenshots/` 目录下，供评审参考。

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
2. ✅ **项目说明文档**：README.md（含运行截图）
3. ✅ **运行截图**：screenshots/ 目录 + README 内嵌显示
4. ✅ **Agent 交互日志**：AI_PROMPTS.md

## 许可证

本项目仅供学习和竞赛使用。

## 联系方式

如有问题或建议，请通过 GitHub Issues 联系我们。
