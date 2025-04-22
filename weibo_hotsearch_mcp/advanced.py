"""
微博热搜 MCP 服务 (高级版)

这个服务使用FastMCP将weibo_hotsearch.py转换为MCP服务，
提供获取微博热搜的功能，并增加了更多高级功能。
"""

from fastmcp import FastMCP, Context
from . import weibo_hotsearch
import time
from typing import Optional, List, Dict

# 创建MCP服务
mcp = FastMCP("微博热搜高级版", dependencies=["httpx", "asyncio"])

# 缓存热搜数据，避免频繁请求
cache = {
    "data": None,
    "timestamp": 0,
    "ttl": 300  # 缓存有效期5分钟
}

def get_cached_hot_search() -> List[str]:
    """获取缓存的热搜数据，如果缓存过期则重新获取"""
    current_time = time.time()
    if cache["data"] is None or (current_time - cache["timestamp"]) > cache["ttl"]:
        try:
            cache["data"] = weibo_hotsearch.get_weibo_hot()
            cache["timestamp"] = current_time
        except Exception as e:
            if cache["data"] is None:  # 如果没有缓存数据，则抛出异常
                raise e
            # 如果有缓存数据，则使用旧数据并记录错误
            print(f"获取热搜失败，使用缓存数据: {str(e)}")
    return cache["data"]

@mcp.tool()
def get_weibo_hot(ctx: Context) -> List[str]:
    """
    获取微博热搜榜前10条内容

    参数:
        ctx: MCP上下文对象，用于记录日志和状态
    """
    ctx.info("正在获取微博热搜...")
    result = get_cached_hot_search()
    ctx.info(f"成功获取{len(result)}条热搜")
    return result

@mcp.tool()
def get_top_n_hot(ctx: Context, n: int = 5) -> List[str]:
    """
    获取微博热搜榜前N条内容

    参数:
        ctx: MCP上下文对象，用于记录日志和状态
        n: 要获取的热搜条数，默认为5条
    """
    ctx.info(f"正在获取微博热搜前{n}条...")
    result = get_cached_hot_search()
    return result[:min(n, len(result))]

@mcp.tool()
def search_hot_topics(ctx: Context, keyword: str) -> List[str]:
    """
    搜索包含指定关键词的热搜条目

    参数:
        ctx: MCP上下文对象，用于记录日志和状态
        keyword: 要搜索的关键词
    """
    ctx.info(f"正在搜索包含'{keyword}'的热搜...")
    result = get_cached_hot_search()
    matched = [item for item in result if keyword.lower() in item.lower()]
    ctx.info(f"找到{len(matched)}条匹配的热搜")
    return matched

@mcp.resource("weibo://hotsearch")
def get_weibo_hot_resource() -> List[str]:
    """获取微博热搜榜前10条内容作为资源"""
    return get_cached_hot_search()

@mcp.resource("weibo://hotsearch/{count}")
def get_weibo_hot_count(count: int) -> List[str]:
    """获取指定数量的微博热搜条目"""
    try:
        count_num = int(count)
        result = get_cached_hot_search()
        return result[:min(count_num, len(result))]
    except ValueError:
        return ["参数错误：count必须是整数"]

@mcp.prompt()
def ask_about_hot_topics() -> str:
    """生成一个关于热门话题的提示"""
    return "请分析当前微博热搜榜上的热门话题，并解释为什么这些话题会受到关注。"

@mcp.prompt()
def compare_hot_topics() -> str:
    """生成一个比较热门话题的提示"""
    return "请比较当前微博热搜榜上的前三个话题，分析它们的共同点和差异，以及它们反映的社会关注点。"

@mcp.tool()
def get_hot_search_stats(ctx: Context) -> Dict:
    """
    获取热搜统计信息

    参数:
        ctx: MCP上下文对象，用于记录日志和状态
    """
    ctx.info("正在分析热搜数据...")
    hot_list = get_cached_hot_search()

    # 简单的统计分析
    word_count = {}
    total_chars = 0

    for item in hot_list:
        total_chars += len(item)
        words = item.split()
        for word in words:
            if len(word) > 1:  # 忽略单字符
                word_count[word] = word_count.get(word, 0) + 1

    # 找出最常见的词
    common_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]

    return {
        "total_topics": len(hot_list),
        "average_length": total_chars / len(hot_list) if hot_list else 0,
        "common_words": [word for word, _ in common_words],  # 使用下划线忽略未使用的变量
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(cache["timestamp"]))
    }

def run():
    """启动高级版MCP服务"""
    mcp.run()

# 如果直接运行此脚本，启动MCP服务
if __name__ == "__main__":
    run()
