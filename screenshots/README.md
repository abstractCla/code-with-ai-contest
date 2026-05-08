# Screenshots 目录

此目录存放 5G 信号可视化看板的运行截图。

## 截图列表

| 文件名 | 展示内容 | 截图描述 |
|--------|----------|----------|
| `main_dashboard.png` | 主页面与2D地图 | 标题、指标卡片、2D信号分布地图、侧边栏筛选器 |
| `3d_map_charts.png` | 3D地图与统计图表 | 3D HexagonLayer 地图、频段分布柱状图、终端类型占比 |
| `rsrp_sinr_scatter.png` | RSRP-SINR关系分析 | RSRP与SINR关系散点图、原始数据预览表格 |
| `band_filter.png` | 频段筛选器 | 频段下拉菜单（n28/n41/n78）|
| `terminal_filter.png` | 终端类型筛选器 | 终端类型下拉菜单（CPE/IoT/Smartphone）|

## 截图内容说明

### main_dashboard.png
- 应用主界面标题和欢迎信息
- 四个关键指标卡片（总数据点、平均RSRP、平均SINR、平均下载速率）
- 2D信号分布地图（根据RSRP着色：绿色> -90dBm，红色< -110dBm）
- 左侧侧边栏完整展示

### 3d_map_charts.png
- 3D HexagonLayer 可视化效果
- 六边形高度随下载速率变化
- 频段分布柱状图
- 终端类型占比柱状图

### rsrp_sinr_scatter.png
- RSRP与SINR关系散点图
- 原始数据预览表格（前20行）

### band_filter.png
- 频段筛选下拉菜单
- 选项：全部、n28、n41、n78

### terminal_filter.png
- 终端类型筛选下拉菜单
- 选项：全部、CPE、IoT、Smartphone

## 截图方法

1. 启动应用：`streamlit run app.py`
2. 打开浏览器访问：`http://localhost:8501`
3. 使用系统截图工具截取所需界面
4. 按上述命名规则保存至本目录

## 文件命名规范

- 使用小写字母和下划线
- 描述性文件名，便于识别
- 使用 `.png` 格式
