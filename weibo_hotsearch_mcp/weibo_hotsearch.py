import httpx
import asyncio
import time
import traceback
import sys
from typing import List, Dict, Any

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
        print(f"开始请求微博热搜 API: {HOT_SEARCH_URL}")
        print(f"请求头: {DEFAULT_HEADERS}")

        async with httpx.AsyncClient() as client:
            response = await client.get(HOT_SEARCH_URL, headers=DEFAULT_HEADERS, timeout=10.0)
            print(f"响应状态码: {response.status_code}")

            if response.status_code == 200:
                result = response.json()
                print(f"响应数据类型: {type(result)}")
                print(f"响应数据结构: {list(result.keys()) if isinstance(result, dict) else 'Not a dict'}")

                # 检查响应是否包含有效数据
                if result.get('ok') == 1 and 'data' in result and 'cards' in result['data']:
                    print(f"'ok' 字段存在且为1，'data' 和 'cards' 字段也存在")
                    print(f"cards 数量: {len(result['data']['cards'])}")

                    hot_searches = []

                    # 提取热搜数据
                    for i, card in enumerate(result['data']['cards']):
                        print(f"Processing card {i+1}/{len(result['data']['cards'])}")
                        if 'card_group' in card:
                            print(f"card_group 存在，包含 {len(card['card_group'])} 个项目")
                            for j, item in enumerate(card['card_group']):
                                print(f"  检查项目 {j+1}/{len(card['card_group'])}: 字段 = {list(item.keys())}")
                                if 'desc' in item:
                                    print(f"  找到 'desc' 字段: {item['desc']}")
                                    hot_searches.append(item['desc'])
                        else:
                            print(f"card_group 不存在于当前 card，字段 = {list(card.keys())}")

                    print(f"提取到 {len(hot_searches)} 条热搜数据")
                    return hot_searches[:10]  # 只返回前10条
                else:
                    print(f"API 响应格式不符合预期: ok={result.get('ok')}, 字段={list(result.keys())}")
                    if 'data' in result:
                        print(f"data 字段内容: {list(result['data'].keys()) if isinstance(result['data'], dict) else 'Not a dict'}")
                    return ["获取微博热搜失败: 响应格式不符合预期"]
            else:
                return [f"获取微博热搜失败: HTTP状态码 {response.status_code}"]
    except Exception as e:
        error_msg = str(e) if str(e) else "未知异常"
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_str = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        print(f"异步获取热搜异常: {error_msg}")
        print(f"异常详情:\n{tb_str}")
        return [f"获取微博热搜失败: {error_msg}"]

def get_weibo_hot() -> List[str]:
    """
    同步获取微博热搜榜前10条内容

    Returns:
        List[str]: 热搜列表，如果获取失败则返回错误信息
    """
    # 添加重试机制
    for i in range(3):  # 最多重试3次
        try:
            # 检查是否已有事件循环
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                # 如果没有事件循环，创建一个新的
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

            # 使用现有事件循环运行异步函数
            if loop.is_running():
                # 如果事件循环已经在运行，使用create_task和Future
                future = asyncio.run_coroutine_threadsafe(get_weibo_hot_async(), loop)
                return future.result(10)  # 10秒超时
            else:
                # 如果事件循环没有运行，使用run_until_complete
                return loop.run_until_complete(get_weibo_hot_async())
        except Exception as e:
            error_msg = str(e) if str(e) else "未知异常"
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb_str = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
            print(f"同步获取热搜异常 (重试{i+1}/3): {error_msg}")
            print(f"异常详情:\n{tb_str}")
            if i == 2:  # 最后一次重试仍失败
                return [f"获取微博热搜失败: {error_msg}"]
            time.sleep(2)  # 等待2秒后重试

    # 如果异步方式失败，尝试使用同步方式
    print("异步方式失败，尝试使用同步方式获取热搜数据")
    try:
        with httpx.Client() as client:
            print(f"开始同步请求微博热搜 API: {HOT_SEARCH_URL}")
            response = client.get(HOT_SEARCH_URL, headers=DEFAULT_HEADERS, timeout=10.0)
            print(f"响应状态码: {response.status_code}")

            if response.status_code == 200:
                result = response.json()
                print(f"响应数据类型: {type(result)}")

                if result.get('ok') == 1 and 'data' in result and 'cards' in result['data']:
                    hot_searches = []

                    for card in result['data']['cards']:
                        if 'card_group' in card:
                            for item in card['card_group']:
                                if 'desc' in item:
                                    hot_searches.append(item['desc'])

                    if hot_searches:
                        print(f"同步方式提取到 {len(hot_searches)} 条热搜数据")
                        return hot_searches[:10]

        return ["获取微博热搜失败: 同步方式也失败"]
    except Exception as e:
        error_msg = str(e) if str(e) else "未知异常"
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_str = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        print(f"同步备用方式异常: {error_msg}")
        print(f"异常详情:\n{tb_str}")
        return [f"获取微博热搜失败: 所有方式均失败"]

if __name__ == '__main__':
    hot_list = get_weibo_hot()
    for i, item in enumerate(hot_list, 1):
        print(f"{i}. {item}")
