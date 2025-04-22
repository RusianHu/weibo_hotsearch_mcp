from setuptools import setup, find_packages
import os

# 读取README.md文件内容作为长描述
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="weibo-hotsearch-mcp",
    version="0.1.0",
    author="RusianHu",
    author_email="your.email@example.com",  # 请替换为你的邮箱
    description="微博热搜MCP服务",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/weibo_hotsearch_mcp",  # 请替换为你的GitHub仓库地址
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "fastmcp>=2.0.0",
        "requests",
        "beautifulsoup4",
    ],
    entry_points={
        "console_scripts": [
            "weibo-mcp=weibo_hotsearch_mcp.cli:main",
            "weibo-mcp-basic=weibo_hotsearch_mcp.basic:run",
            "weibo-mcp-advanced=weibo_hotsearch_mcp.advanced:run",
        ],
    },
)
