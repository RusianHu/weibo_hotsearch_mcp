"""
微博热搜 MCP 服务

基于 fastmcp 创建的微博热搜 MCP 服务，可以在 Claude 等 AI 助手中使用。
"""

from fastmcp import FastMCP
from weibo_hotsearch_no_cookie import get_weibo_hot
from typing import List

# 创建 MCP 服务
mcp = FastMCP("微博热搜")

@mcp.tool()
def get_hot_search() -> List[str]:
    """
    获取微博热搜榜前10条内容

    Returns:
        List[str]: 热搜列表，如果获取失败则返回错误信息
    """
    return get_weibo_hot()

@mcp.resource("weibo://hot-search")
def get_hot_search_resource() -> List[str]:
    """
    获取微博热搜榜前10条内容作为资源

    Returns:
        List[str]: 热搜列表，如果获取失败则返回错误信息
    """
    return get_weibo_hot()

@mcp.prompt()
def hot_search_prompt() -> str:
    """生成一个标准的微博热搜请求提示"""
    return "请获取当前微博热搜榜的内容，并分析一下热门话题的类别分布。"

def main():
    """CLI 入口点"""
    mcp.run()

if __name__ == "__main__":
    main()
