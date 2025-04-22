import httpx
import asyncio
import time
from typing import List

# 热搜API端点 - 微博移动版API，无需Cookie
HOT_SEARCH_URL = 'https://m.weibo.cn/api/container/getIndex?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot'

# 请求头 - 不包含Cookie
DEFAULT_HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

async def get_weibo_hot_async() -> List[str]:
    """
    异步获取微博热搜榜前10条内容

    Returns:
        List[str]: 热搜列表，如果获取失败则返回错误信息
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(HOT_SEARCH_URL, headers=DEFAULT_HEADERS, timeout=10.0)

            if response.status_code == 200:
                result = response.json()

                # 检查响应是否包含有效数据
                if result.get('ok') == 1 and 'data' in result and 'cards' in result['data']:
                    hot_searches = []

                    # 提取热搜数据
                    for card in result['data']['cards']:
                        if 'card_group' in card:
                            for item in card['card_group']:
                                if 'desc' in item:
                                    hot_searches.append(item['desc'])

                    return hot_searches[:10]  # 只返回前10条
                else:
                    return ["获取微博热搜失败: 响应格式不符合预期"]
            else:
                return [f"获取微博热搜失败: HTTP状态码 {response.status_code}"]
    except Exception as e:
        return [f"获取微博热搜失败: {str(e)}"]

def get_weibo_hot() -> List[str]:
    """
    同步获取微博热搜榜前10条内容

    Returns:
        List[str]: 热搜列表，如果获取失败则返回错误信息
    """
    # 添加重试机制
    for i in range(3):  # 最多重试3次
        try:
            return asyncio.run(get_weibo_hot_async())
        except Exception as e:
            if i == 2:  # 最后一次重试仍失败
                return [f"获取微博热搜失败: {str(e)}"]
            time.sleep(2)  # 等待2秒后重试

    return ["获取微博热搜失败: 未知错误"]

if __name__ == '__main__':
    hot_list = get_weibo_hot()
    for i, item in enumerate(hot_list, 1):
        print(f"{i}. {item}")