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

### 3.1 安装方式：通过 pip 从 GitHub 安装

您可以直接通过 pip 从 GitHub 安装本项目：

```bash
pip install git+https://github.com/RusianHu/weibo_hotsearch_mcp.git
```

如果您需要使用代理，可以添加代理参数：

```bash
pip install git+https://github.com/RusianHu/weibo_hotsearch_mcp.git --proxy socks5://127.0.0.1:10808
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

### 3.2 验证安装

安装完成后，您可以通过以下命令验证安装是否成功：

```bash
pip list | findstr weibo
```

如果安装成功，您将看到类似以下输出：

```
weibo-hotsearch-mcp 0.1.0
```

您也可以通过导入包来验证安装：

```python
import weibo_hotsearch_mcp
print("安装成功")
```

### 3.3 安装位置

通过 pip 安装后，包文件将被安装到 Python 的 site-packages 目录中，具体路径取决于您的 Python 安装位置，通常类似于：

```
C:\Users\<用户名>\AppData\Local\Programs\Python\Python<版本>\Lib\site-packages\weibo_hotsearch_mcp
```

或

```
C:\Python<版本>\Lib\site-packages\weibo_hotsearch_mcp
```

可执行文件将被安装到 Python 的 Scripts 目录中，同样取决于您的 Python 安装位置：

```
C:\Users\<用户名>\AppData\Local\Programs\Python\Python<版本>\Scripts\
```

或

```
C:\Python<版本>\Scripts\
```

您可以通过以下命令查看包的具体安装位置：

```bash
pip show -f weibo-hotsearch-mcp
```

## 四、配置Cookie数据

本服务需要通过环境变量传递Cookie数据才能正常工作。这是出于以下原因：

- 微博网站需要Cookie才能正常访问热搜数据
- 保护用户隐私，避免在代码中硬编码Cookie
- 允许用户使用自己的微博账号权限获取数据

### 4.1 通过mcp_settings.json配置Cookie（必需）

**重要提示：** 要使用微博热搜服务，必须配置 WEIBO_COOKIE 环境变量，否则服务将无法获取微博热搜数据。

1. 打开MCP配置文件（位于`%APPDATA%\Code\User\globalStorage\rooveterinaryinc.roo-cline\settings\mcp_settings.json`）
2. 在微博热搜服务配置中添加`env`对象，如下所示：

```json
"weibo-hotsearch": {
  "command": "weibo-mcp-advanced",
  "disabled": false,
  "env": {
    "WEIBO_COOKIE": "你的微博Cookie数据"
  },
  "alwaysAllow": []
}
```

3. 将`"你的微博Cookie数据"`替换为您的实际Cookie值

### 4.2 获取微博Cookie

1. 登录微博网站(https://weibo.com)
2. 在浏览器中打开开发者工具（按F12或右键点击页面并选择"检查"）
3. 切换到"网络"(Network)选项卡
4. 刷新页面
5. 在请求列表中找到任意一个请求，点击它
6. 在请求头(Headers)中找到"Cookie"字段
7. 复制完整的Cookie值

**注意**：Cookie中包含敏感信息，请勿分享给他人或在公共场合暴露。

## 五、在Claude Desktop中使用

安装完成后，MCP服务将自动在Claude Desktop中注册。使用步骤如下：

1. 打开Claude Desktop应用
2. 在对话框中，点击右下角的"+"按钮
3. 在弹出的菜单中选择"微博热搜"或"微博热搜高级版"
4. 现在您可以在对话中使用微博热搜服务了

## 六、在CLine插件中配置（VSCode、JetBrains等）

### 6.1 VSCode中配置CLine插件

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
  "command": "weibo-mcp-advanced",
  "disabled": false,
  "env": {
    "WEIBO_COOKIE": "你的微博Cookie数据"
  },
  "alwaysAllow": []
}
```

注意：
- 使用 pip 安装后，可以直接使用命令名称而不需要指定完整路径
- 如果您使用的是基础版，请将命令改为 `weibo-mcp-basic`

### 6.2 JetBrains IDE中配置CLine插件

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
  "command": "weibo-mcp-basic",
  "disabled": false,
  "env": {
    "WEIBO_COOKIE": "你的微博Cookie数据"
  },
  "alwaysAllow": []
}
```

**高级版：**
```json
"weibo-hotsearch-advanced": {
  "command": "weibo-mcp-advanced",
  "disabled": false,
  "env": {
    "WEIBO_COOKIE": "你的微博Cookie数据"
  },
  "alwaysAllow": []
}
```

### 6.3 RooCode插件配置

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
  "command": "weibo-mcp-basic",
  "disabled": false,
  "env": {
    "WEIBO_COOKIE": "你的微博Cookie数据"
  },
  "alwaysAllow": []
}
```

**高级版：**
```json
"weibo-hotsearch-advanced": {
  "command": "weibo-mcp-advanced",
  "disabled": false,
  "env": {
    "WEIBO_COOKIE": "你的微博Cookie数据"
  },
  "alwaysAllow": []
}
```

## 七、使用示例

安装并配置完成后，您可以在Claude中使用以下提示来获取微博热搜：

### 7.1 基础版使用示例

1. "获取当前微博热搜榜"
2. "分析当前微博热搜话题"
3. "查看微博热门话题"

### 7.2 高级版使用示例

1. "获取前5条微博热搜"
2. "搜索包含'电影'的热搜话题"
3. "获取微博热搜统计信息"
4. "比较当前热门话题的异同点"

Claude将调用MCP服务获取最新的微博热搜数据并进行回复。

## 八、故障排除

如果遇到问题，请尝试以下解决方法：

1. **服务无法启动**：
   - 检查Python环境是否正确
   - 确认所有依赖包已安装
   - 检查网络连接
   - 尝试重新安装包：`pip install git+https://github.com/RusianHu/weibo_hotsearch_mcp.git --force-reinstall`

2. **无法获取热搜数据**：
   - 检查是否已设置 WEIBO_COOKIE 环境变量（这是必需的）
   - 确认设置的Cookie是否有效（Cookie可能会过期）
   - 检查网络连接
   - 确认微博网站是否可访问

3. **Claude无法识别服务**：
   - 重新安装MCP服务
   - 重启Claude Desktop应用
   - 检查CLine插件配置是否正确
   - 确认命令行可以正常启动服务：`weibo-mcp-advanced`

4. **找不到命令**：
   - 确认Python的Scripts目录已添加到系统环境变量中
   - 尝试使用完整路径运行命令，例如：`C:\Users\<用户名>\AppData\Local\Programs\Python\Python<版本>\Scripts\weibo-mcp-advanced.exe`
   - 重新安装包并检查是否有错误信息

## 九、高级配置

### 9.1 自定义服务名称

如果您想在从源代码安装时使用不同的服务名称，可以修改安装命令中的`--name`参数：

```
python -m fastmcp install weibo_hotsearch_mcp.py --name "自定义名称" --with requests --with beautifulsoup4
```

注意：通过pip安装时，服务名称已固定为"微博热搜"（基础版）和"微博热搜高级版"（高级版）。

### 9.2 修改热搜数量

在高级版中，您可以使用 `get_top_n_hot` 工具指定要获取的热搜数量，无需修改代码。

### 9.3 自定义缓存时间

在高级版中，缓存有效期默认为5分钟（300秒）。如果您需要修改缓存时间，可以编辑安装目录中的 `weibo_hotsearch_mcp/advanced.py` 文件，找到并修改以下代码行：

```python
cache = {
    "data": None,
    "timestamp": 0,
    "ttl": 300  # 缓存有效期5分钟，可以根据需要调整此值
}
```

## 十、许可证

本项目采用 [MIT 许可证](./LICENSE) 开源。
