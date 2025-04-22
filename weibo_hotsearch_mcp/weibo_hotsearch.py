import requests
from bs4 import BeautifulSoup
import time
import os

def get_headers():
    # 从环境变量中获取Cookie，如果没有则使用默认值
    default_cookie = 'SUB=_114514'
    cookie = os.environ.get('WEIBO_COOKIE', default_cookie)

    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Cookie': cookie,
        'Referer': 'https://weibo.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

def get_weibo_hot():
    url = 'https://s.weibo.com/top/summary'
    try:
        # 添加重试机制和延迟
        for i in range(3):  # 最多重试3次
            try:
                # 显式禁用代理
                session = requests.Session()
                session.trust_env = False  # 不读取系统代理设置
                response = session.get(url, headers=get_headers(), timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    hot_items = soup.select('.td-02 a')
                    return [item.text for item in hot_items[:10]]  # 返回前10条热搜
                else:
                    time.sleep(2)  # 等待2秒后重试
            except Exception as e:
                if i == 2:  # 最后一次重试仍失败
                    raise
                time.sleep(2)
        return "获取微博热搜失败: 请求未成功"
    except Exception as e:
        return f"获取微博热搜失败: {str(e)}"

if __name__ == '__main__':
    hot_list = get_weibo_hot()
    for i, item in enumerate(hot_list, 1):
        print(f"{i}. {item}")
