from setuptools import setup, find_packages
import os

# 读取README.md文件内容作为长描述
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="weibo-hotsearch-mcp",
    version="1.0.0",
    author="RusianHu",
    author_email="rusianhu@example.com",
    description="微博热搜MCP服务",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RusianHu/weibo_hotsearch_mcp",
    project_urls={
        "Bug Tracker": "https://github.com/RusianHu/weibo_hotsearch_mcp/issues",
        "Source Code": "https://github.com/RusianHu/weibo_hotsearch_mcp",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "fastmcp>=2.0.0",
        "httpx",
        "asyncio",
    ],
    entry_points={
        "console_scripts": [
            "weibo-mcp=weibo_hotsearch_mcp.cli:main",
            "weibo-mcp-basic=weibo_hotsearch_mcp.basic:run",
            "weibo-mcp-advanced=weibo_hotsearch_mcp.advanced:run",
        ],
    },
)
