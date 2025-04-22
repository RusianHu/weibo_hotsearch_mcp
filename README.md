# 微博热搜MCP服务

一个简单的微博热搜MCP服务，你可以在Claude AI中使用。本服务提供基础版和高级版两个版本，您可以根据需要选择安装。

## 一、服务功能说明

### 1.1 基础版功能

基础版MCP服务提供以下功能：

1. **工具(Tool)**: `get_weibo_hot` - 获取微博热搜榜前10条内容
2. **资源(Resource)**: `weibo://hotsearch` - 提供微博热搜数据作为资源
3. **提示(Prompt)**: `ask_about_hot_topics` - 生成关于热门话题的提示

### 1.2 高级版功能

高级版MCP服务在基础版的基础上，增加了以下功能：

1. **工具(Tool)**:
   - `get_weibo_hot` - 获取微博热搜榜前10条内容，并带有日志记录
   - `get_top_n_hot` - 获取指定数量的微博热搜条目
   - `search_hot_topics` - 搜索包含指定关键词的热搜条目
   - `get_hot_search_stats` - 获取热搜统计信息

2. **资源(Resource)**:
   - `weibo://hotsearch` - 提供微博热搜数据作为资源
   - `weibo://hotsearch/{count}` - 获取指定数量的微博热搜条目

3. **提示(Prompt)**:
   - `ask_about_hot_topics` - 生成关于热门话题的提示
   - `compare_hot_topics` - 生成比较热门话题的提示

4. **高级特性**:
   - 数据缓存 - 避免频繁请求微博服务器
   - 错误处理 - 更健壮的错误处理机制
   - 进度报告 - 在处理过程中提供进度更新

## 二、准备工作

### 2.1 环境要求

- Python 3.10 或更高版本
- pip 包管理器
- 网络连接（用于获取微博热搜数据）

### 2.2 依赖包

- fastmcp：MCP服务框架
- requests：网络请求库
- beautifulsoup4：HTML解析库

## 三、安装步骤

### 3.1 安装方式一：通过 pip 从 GitHub 安装（推荐）

您可以直接通过 pip 从 GitHub 安装本项目：

```bash
pip install git+https://github.com/RusianHu/weibo_hotsearch_mcp.git
```

安装完成后，您可以通过以下命令启动服务：

**基础版：**
```bash
weibo-mcp-basic
```

**高级版：**
```bash
weibo-mcp-advanced
```

或者使用通用命令（默认启动基础版，使用 `--advanced` 参数启动高级版）：
```bash
weibo-mcp
```
```bash
weibo-mcp --advanced
```

### 3.2 安装方式二：使用安装脚本

1. 确保您已下载本项目的所有文件
2. 双击运行 `install_weibo_mcp.bat` 脚本
3. 选择要安装的版本（基础版或高级版）
4. 等待安装完成

### 3.3 安装方式三：手动安装

1. 打开命令提示符或PowerShell
2. 切换到项目目录
3. 执行以下命令：

   **基础版：**
   ```
   python -m fastmcp install weibo_hotsearch_mcp.py --name "微博热搜" --with requests --with beautifulsoup4
   ```

   **高级版：**
   ```
   python -m fastmcp install weibo_hotsearch_mcp_advanced.py --name "微博热搜高级版" --with requests --with beautifulsoup4
   ```

## 四、在Claude Desktop中使用

安装完成后，MCP服务将自动在Claude Desktop中注册。使用步骤如下：

1. 打开Claude Desktop应用
2. 在对话框中，点击右下角的"+"按钮
3. 在弹出的菜单中选择"微博热搜"或"微博热搜高级版"
4. 现在您可以在对话中使用微博热搜服务了

## 五、在CLine插件中配置（VSCode、JetBrains等）

### 5.1 VSCode中配置CLine插件

1. 确保已安装CLine插件
2. 找到CLine的MCP配置文件，位于：
   ```
   %APPDATA%\Code\User\globalStorage\rooveterinaryinc.roo-cline\settings\mcp_settings.json
   ```
   在Windows系统中，通常路径为：
   ```
   C:\Users\<用户名>\AppData\Roaming\Code\User\globalStorage\rooveterinaryinc.roo-cline\settings\mcp_settings.json
   ```
3. 编辑该文件，在`mcpServers`对象中添加以下配置：

```json
"weibo-hotsearch": {
  "command": "cmd",
  "args": [
    "/c",
    "python",
    "{weibo_hotsearch_mcp}\\weibo_hotsearch_mcp_advanced.py"
  ],
  "disabled": false,
  "alwaysAllow": []
}
```

注意：
- 注意：将路径中的`{weibo_hotsearch_mcp}`替换为您的weibo_hotsearch_mcp文件夹目录
- 如果您使用的是基础版，请将路径中的`weibo_hotsearch_mcp_advanced.py`替换为`weibo_hotsearch_mcp.py`

### 5.2 JetBrains IDE中配置CLine插件

1. 确保已安装CLine插件
2. 在JetBrains IDE中，CLine插件使用与VSCode相同的配置文件
3. 找到CLine的MCP配置文件，位于：
   ```
   %APPDATA%\Code\User\globalStorage\rooveterinaryinc.roo-cline\settings\mcp_settings.json
   ```
4. 编辑该文件，在`mcpServers`对象中添加微博热搜服务配置（与VSCode配置相同）

**基础版：**
```json
"weibo-hotsearch": {
  "command": "cmd",
  "args": [
    "/c",
    "python",
    "{weibo_hotsearch_mcp}\\weibo_hotsearch_mcp.py"
  ],
  "disabled": false,
  "alwaysAllow": []
}
```

**高级版：**
```json
"weibo-hotsearch-advanced": {
  "command": "cmd",
  "args": [
    "/c",
    "python",
    "{weibo_hotsearch_mcp}\\weibo_hotsearch_mcp_advanced.py"
  ],
  "disabled": false,
  "alwaysAllow": []
}
```

注意：将路径中的`<用户名>`替换为您的Windows用户名

### 5.3 RooCode插件配置

1. 确保已安装RooCode插件
2. RooCode插件也使用与CLine相同的MCP配置文件
3. 找到MCP配置文件，位于：
   ```
   %APPDATA%\Code\User\globalStorage\rooveterinaryinc.roo-cline\settings\mcp_settings.json
   ```
4. 编辑该文件，在`mcpServers`对象中添加微博热搜服务配置（与VSCode配置相同）

**基础版：**
```json
"weibo-hotsearch": {
  "command": "cmd",
  "args": [
    "/c",
    "python",
    "{weibo_hotsearch_mcp}\\weibo_hotsearch_mcp.py"
  ],
  "disabled": false,
  "alwaysAllow": []
}
```

**高级版：**
```json
"weibo-hotsearch-advanced": {
  "command": "cmd",
  "args": [
    "/c",
    "python",
    "{weibo_hotsearch_mcp}\\weibo_hotsearch_mcp_advanced.py"
  ],
  "disabled": false,
  "alwaysAllow": []
}
```

注意：将路径中的`{weibo_hotsearch_mcp}`替换为您的weibo_hotsearch_mcp文件夹目录

## 六、使用示例

安装并配置完成后，您可以在Claude中使用以下提示来获取微博热搜：

### 6.1 基础版使用示例

1. "获取当前微博热搜榜"
2. "分析当前微博热搜话题"
3. "查看微博热门话题"

### 6.2 高级版使用示例

1. "获取前5条微博热搜"
2. "搜索包含'电影'的热搜话题"
3. "获取微博热搜统计信息"
4. "比较当前热门话题的异同点"

Claude将调用MCP服务获取最新的微博热搜数据并进行回复。

## 七、故障排除

如果遇到问题，请尝试以下解决方法：

1. **服务无法启动**：
   - 检查Python环境是否正确
   - 确认所有依赖包已安装
   - 检查网络连接

2. **无法获取热搜数据**：
   - 检查网络连接
   - 确认微博网站是否可访问
   - 检查weibo_hotsearch.py文件是否存在并正确配置

3. **Claude无法识别服务**：
   - 重新安装MCP服务
   - 重启Claude Desktop应用
   - 检查CLine插件配置是否正确

## 八、高级配置

### 8.1 自定义服务名称

如果您想使用不同的服务名称，可以修改安装命令中的`--name`参数：

```
python -m fastmcp install weibo_hotsearch_mcp.py --name "自定义名称" --with requests --with beautifulsoup4
```

### 8.2 修改热搜数量

如果您想修改返回的热搜数量，可以编辑`weibo_hotsearch.py`文件中的相关代码。

### 8.3 自定义缓存时间

在高级版中，您可以通过修改`weibo_hotsearch_mcp_advanced.py`文件中的`cache["ttl"]`值来调整缓存有效期。

### 8.4 自定义Cookie数据

您可以通过环境变量传递自定义的Cookie数据，而不是使用代码中硬编码的默认值。这在以下情况特别有用：

- 当默认Cookie过期或失效时
- 需要使用自己的微博账号权限获取更多数据时
- 在不同环境中部署服务时

#### 8.4.1 通过mcp_settings.json配置Cookie

1. 打开MCP配置文件（位于`%APPDATA%\Code\User\globalStorage\rooveterinaryinc.roo-cline\settings\mcp_settings.json`）
2. 在微博热搜服务配置中添加`env`对象，如下所示：

```json
"weibo-hotsearch": {
  "command": "cmd",
  "args": [
    "/c",
    "python",
    "{weibo_hotsearch_mcp}\\weibo_hotsearch_mcp_advanced.py"
  ],
  "disabled": false,
  "env": {
    "WEIBO_COOKIE": "你的微博Cookie数据"
  },
  "alwaysAllow": []
}
```

3. 将`"你的微博Cookie数据"`替换为您的实际Cookie值

#### 8.4.2 获取微博Cookie

1. 登录微博网站(https://weibo.com)
2. 在浏览器中打开开发者工具（按F12或右键点击页面并选择"检查"）
3. 切换到"网络"(Network)选项卡
4. 刷新页面
5. 在请求列表中找到任意一个请求，点击它
6. 在请求头(Headers)中找到"Cookie"字段
7. 复制完整的Cookie值

**注意**：Cookie中包含敏感信息，请勿分享给他人或在公共场合暴露。

#### 8.4.3 其他MCP服务的Cookie配置

同样的方法也适用于其他MCP服务，如高德地图服务等。您只需要在相应的服务配置中添加`env`对象，并设置所需的环境变量即可。例如：

```json
"amap-amap-sse": {
  "url": "https://mcp.amap.com/sse?key=YOUR_API_KEY",
  "env": {
    "COOKIE": "你的高德地图Cookie数据"
  }
}
```

## 九、许可证

本项目采用 [MIT 许可证](./LICENSE) 开源。MIT 许可证是一种宽松的软件许可证，它允许任何人以任何方式使用本代码，只要保留原始许可证和版权声明。

### 9.1 MIT 许可证主要条款

- 允许任何人自由使用、复制、修改、合并、发布、分发、再许可和/或销售本软件的副本
- 要求在所有副本或实质性使用本软件的地方包含原始许可证和版权声明
- 软件按"原样"提供，不提供任何形式的保证

### 9.2 使用本项目

如果您想在自己的项目中使用本代码，只需确保：

1. 包含原始的 LICENSE 文件
2. 保留原始的版权声明

完整的许可证文本可以在项目根目录的 [LICENSE](./LICENSE) 文件中找到。