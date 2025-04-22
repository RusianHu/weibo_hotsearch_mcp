"""
微博热搜MCP服务的命令行接口
"""

import argparse
import sys
from . import basic, advanced

def main():
    """命令行入口点"""
    parser = argparse.ArgumentParser(description='微博热搜MCP服务')
    parser.add_argument('--version', '-v', action='version', 
                        version='%(prog)s 0.1.0')
    parser.add_argument('--advanced', '-a', action='store_true',
                        help='启动高级版MCP服务')
    
    args = parser.parse_args()
    
    if args.advanced:
        print("正在启动微博热搜MCP服务(高级版)...")
        advanced.run()
    else:
        print("正在启动微博热搜MCP服务(基础版)...")
        basic.run()

if __name__ == '__main__':
    main()
