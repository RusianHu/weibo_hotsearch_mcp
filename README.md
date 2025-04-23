# 微博热搜 MCP 服务

这是一个基于 [fastmcp](https://github.com/jlowin/fastmcp) 创建的微博热搜 MCP 服务，可以在 Claude 等支持 MCP 协议的 AI 助手中使用。

## 功能

- 获取微博热搜榜前10条内容
- 无需提供 Cookie，使用微博移动版 API

## 安装方法

### 方法一：使用 pip 安装

```bash
# 使用 pip 安装
pip install weibo-hotsearch-mcp

# 如果需要使用代理
pip install weibo-hotsearch-mcp --proxy socks5://127.0.0.1:10808

# 从本地安装
pip install dist/weibo_hotsearch_mcp-1.0.0-py3-none-any.whl
```

### 方法二：从 GitHub 安装

```bash
# 直接从 GitHub 安装
pip install git+https://github.com/RusianHu/weibo_hotsearch_mcp.git

# 如果需要使用代理
pip install git+https://github.com/RusianHu/weibo_hotsearch_mcp.git --proxy socks5://127.0.0.1:10808
```

### 方法三：从源码安装

```bash
# 克隆仓库
git clone https://github.com/RusianHu/weibo_hotsearch_mcp.git
cd weibo_hotsearch_mcp

# 安装依赖
pip install -e .
```

## 安装到 Claude Desktop

推荐使用这种方式安装，它会创建一个隔离的环境，更加可靠：

```bash
# 安装到 Claude Desktop
fastmcp install weibo_hotsearch_mcp.py
```

安装成功后，您可以直接在 Claude Desktop 中使用这个服务。

## 在 Roo Code 插件中配置使用

1. 安装 [Roo Code](https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline) VS Code 插件

2. 打开 VS Code 设置，找到 `mcp_settings.json` 文件
   - 路径通常为：`C:\Users\<用户名>\AppData\Roaming\Code\User\globalStorage\rooveterinaryinc.roo-cline\settings\mcp_settings.json`

3. 在 `mcpServers` 对象中添加以下配置：

```json
"weibo-hotsearch": {
  "command": "python",
  "args": [
    "-m", "weibo_hotsearch_mcp"
  ],
  "alwaysAllow": [
    "get_hot_search"
  ],
  "disabled": false
}
```

4. 保存文件后，重启 VS Code

5. 现在你可以在 Claude 中使用微博热搜 MCP 服务了

## 使用示例

在 Claude 中，你可以这样使用微博热搜 MCP 服务：

```
请获取当前微博热搜榜的内容，并分析一下热门话题的类别分布。
```

## 开发

如果你想修改或扩展这个 MCP 服务，可以按照以下步骤进行：

1. 克隆仓库并安装依赖
2. 修改 `weibo_hotsearch_mcp.py` 文件
3. 使用 `fastmcp dev weibo_hotsearch_mcp.py` 命令测试你的修改
4. 使用 `fastmcp install weibo_hotsearch_mcp.py` 命令安装到 Claude Desktop

## 许可证

[MIT](LICENSE)
