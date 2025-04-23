from setuptools import setup, find_packages

setup(
    name="weibo-hotsearch-mcp",
    version="1.0.0",
    description="微博热搜 MCP 服务",
    author="RusianHu",
    author_email="example@example.com",
    packages=find_packages(),
    py_modules=["weibo_hotsearch_mcp", "weibo_hotsearch_no_cookie"],
    install_requires=[
        "fastmcp>=2.0.0",
        "httpx>=0.28.0",
    ],
    entry_points={
        "console_scripts": [
            "weibo-hotsearch-mcp=weibo_hotsearch_mcp:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
