"""
微博热搜 MCP 服务

这个服务使用FastMCP将weibo_hotsearch.py转换为MCP服务，
提供获取微博热搜的功能。
"""

from fastmcp import FastMCP
import weibo_hotsearch

# 创建MCP服务
mcp = FastMCP("微博热搜", dependencies=["requests", "beautifulsoup4"])

@mcp.tool()
def get_weibo_hot() -> list:
    """获取微博热搜榜前10条内容"""
    return weibo_hotsearch.get_weibo_hot()

@mcp.resource("weibo://hotsearch")
def get_weibo_hot_resource() -> list:
    """获取微博热搜榜前10条内容作为资源"""
    return weibo_hotsearch.get_weibo_hot()

@mcp.prompt()
def ask_about_hot_topics() -> str:
    """生成一个关于热门话题的提示"""
    return "请分析当前微博热搜榜上的热门话题，并解释为什么这些话题会受到关注。"

# 如果直接运行此脚本，启动MCP服务
if __name__ == "__main__":
    mcp.run()
