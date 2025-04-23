"""
打包脚本，用于将微博热搜 MCP 服务打包为 pip 安装包
"""

import os
import shutil
import subprocess

def build_package():
    """构建 pip 安装包"""
    print("开始构建 pip 安装包...")

    # 清理旧的构建文件
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("weibo_hotsearch_mcp.egg-info"):
        shutil.rmtree("weibo_hotsearch_mcp.egg-info")

    # 构建 sdist 和 wheel
    subprocess.run(["python", "setup.py", "sdist", "bdist_wheel"])

    print("构建完成！")
    print("生成的文件在 dist 目录下")
    print("可以使用以下命令安装：")
    print("pip install dist/weibo_hotsearch_mcp-1.0.0-py3-none-any.whl")

if __name__ == "__main__":
    build_package()
