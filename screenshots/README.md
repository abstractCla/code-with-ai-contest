# Screenshots 目录

此目录用于存放 5G 信号可视化看板的运行截图。

## 截图要求

根据比赛要求，需要提供 **2-3 张** Web 应用运行时的截图，展示以下内容：

### 推荐截图内容

1. **地图与侧边栏截图** (`screenshot_01.png`)
   - 展示 2D 地图显示信号分布
   - 展示侧边栏筛选器（频段、终端类型下拉菜单）
   - 展示 RSRP 和 SINR 滑动条

2. **数据统计图表截图** (`screenshot_02.png`)
   - 展示频段分布柱状图
   - 展示终端类型占比柱状图
   - 展示 RSRP 与 SINR 关系散点图

3. **3D 地图效果截图** (`screenshot_03.png`)
   - 展示 pydeck 3D HexagonLayer 效果
   - 展示六边形"站起来"的高度效果

## 截图方法

1. 启动应用：`streamlit run app.py`
2. 打开浏览器访问：`http://localhost:8501`
3. 使用系统截图工具或浏览器截图功能
4. 将截图保存到此目录

## 命名建议

- `screenshot_map.png` - 地图截图
- `screenshot_charts.png` - 图表截图
- `screenshot_3d.png` - 3D 地图截图
