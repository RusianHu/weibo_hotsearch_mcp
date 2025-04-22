"""
测试微博热搜获取功能
"""

from weibo_hotsearch_mcp.weibo_hotsearch import get_weibo_hot

def main():
    print("正在获取微博热搜...")
    hot_list = get_weibo_hot()
    print(f"获取到{len(hot_list)}条热搜:")
    for i, item in enumerate(hot_list, 1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    main()
