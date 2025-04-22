"""
测试微博移动版API获取热搜数据

这个脚本尝试使用微博移动版API(m.weibo.cn)获取热搜数据，
测试是否可以不使用Cookie就获取数据。
"""

import httpx
import asyncio
import json
from typing import List, Dict, Any, Optional

# 定义请求头 - 不包含Cookie
DEFAULT_HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

# 可能的热搜API端点
POSSIBLE_ENDPOINTS = [
    # 热搜榜可能的端点
    'https://m.weibo.cn/api/container/getIndex?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot',
    'https://m.weibo.cn/api/container/getIndex?containerid=106003%26filter_type%3Drealtimehot',
    'https://m.weibo.cn/api/container/getIndex?containerid=106003type=25&t=3&disable_hot=1&filter_type=realtimehot',
    'https://m.weibo.cn/api/container/getIndex?containerid=231583',
    # 搜索热搜的端点
    'https://m.weibo.cn/api/searchall?containerid=100103type=1&q=热搜',
    # 发现页的端点
    'https://m.weibo.cn/api/container/getIndex?containerid=106003type=25&t=3&disable_hot=1',
    # 热门微博的端点
    'https://m.weibo.cn/api/container/getIndex?containerid=102803'
]

async def test_endpoint(client: httpx.AsyncClient, url: str) -> Optional[Dict[str, Any]]:
    """测试一个API端点，看是否能获取数据"""
    try:
        print(f"尝试请求: {url}")
        response = await client.get(url, headers=DEFAULT_HEADERS, timeout=10.0)
        if response.status_code == 200:
            result = response.json()
            # 检查响应是否包含有效数据
            if result.get('ok') == 1 and 'data' in result:
                print(f"✅ 成功获取数据: {url}")
                return result
            else:
                print(f"❌ 响应格式不符合预期: {url}")
                return None
        else:
            print(f"❌ 请求失败，状态码: {response.status_code}, URL: {url}")
            return None
    except Exception as e:
        print(f"❌ 请求异常: {str(e)}, URL: {url}")
        return None

def extract_hot_search_from_response(response_data: Dict[str, Any]) -> List[str]:
    """从响应数据中提取热搜列表"""
    hot_searches = []
    
    # 尝试不同的数据结构模式
    try:
        # 模式1: data -> cards -> card_group
        if 'cards' in response_data.get('data', {}):
            for card in response_data['data']['cards']:
                if 'card_group' in card:
                    for item in card['card_group']:
                        if 'desc' in item:
                            hot_searches.append(item['desc'])
                        elif 'title' in item:
                            hot_searches.append(item['title'])
                        elif 'content1' in item:
                            hot_searches.append(item['content1'])
        
        # 模式2: data -> cards -> mblog -> text
        if not hot_searches and 'cards' in response_data.get('data', {}):
            for card in response_data['data']['cards']:
                if 'mblog' in card and 'text' in card['mblog']:
                    hot_searches.append(card['mblog']['text'])
        
        # 模式3: data -> cards -> title
        if not hot_searches and 'cards' in response_data.get('data', {}):
            for card in response_data['data']['cards']:
                if 'title' in card:
                    hot_searches.append(card['title'])
        
        # 模式4: data -> cards -> card_group -> desc_extr
        if not hot_searches and 'cards' in response_data.get('data', {}):
            for card in response_data['data']['cards']:
                if 'card_group' in card:
                    for item in card['card_group']:
                        if 'desc_extr' in item:
                            hot_searches.append(item['desc_extr'])
        
        # 模式5: data -> cards -> card_group -> desc
        if not hot_searches and 'cards' in response_data.get('data', {}):
            for card in response_data['data']['cards']:
                if 'card_group' in card:
                    for item in card['card_group']:
                        if 'desc' in item:
                            hot_searches.append(item['desc'])
    except Exception as e:
        print(f"提取热搜数据时出错: {str(e)}")
    
    return hot_searches[:10]  # 只返回前10条

async def main():
    """主函数，测试所有可能的端点"""
    print("开始测试微博移动版API获取热搜数据...")
    print("不使用Cookie进行测试\n")
    
    async with httpx.AsyncClient() as client:
        for endpoint in POSSIBLE_ENDPOINTS:
            result = await test_endpoint(client, endpoint)
            if result:
                # 尝试从响应中提取热搜数据
                hot_searches = extract_hot_search_from_response(result)
                if hot_searches:
                    print("\n成功从以下端点获取热搜数据:")
                    print(endpoint)
                    print("\n热搜列表:")
                    for i, item in enumerate(hot_searches, 1):
                        print(f"{i}. {item}")
                    print("\n完整响应数据(部分):")
                    print(json.dumps(result, ensure_ascii=False, indent=2)[:1000] + "...")
                    
                    # 保存成功的端点和数据到文件
                    with open("successful_endpoint.txt", "w", encoding="utf-8") as f:
                        f.write(f"成功的端点: {endpoint}\n\n")
                        f.write("热搜列表:\n")
                        for i, item in enumerate(hot_searches, 1):
                            f.write(f"{i}. {item}\n")
                    
                    print("\n已将成功的端点和数据保存到 successful_endpoint.txt")
                    break
                else:
                    print(f"⚠️ 无法从响应中提取热搜数据: {endpoint}\n")
            else:
                print(f"继续尝试下一个端点...\n")
    
    print("\n测试完成。")

if __name__ == "__main__":
    asyncio.run(main())
