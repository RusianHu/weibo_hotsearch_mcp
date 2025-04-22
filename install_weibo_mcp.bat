@echo off
chcp 65001 >nul
echo 微博热搜MCP服务安装脚本
echo ============================
echo 请选择要安装的版本:
echo 1. 基础版
echo 2. 高级版
echo ============================

set /p version=请输入选项(1或2):

if "%version%"=="1" (
    echo 正在安装微博热搜MCP服务(基础版)...
    python -m fastmcp install weibo_hotsearch_mcp.py --name "微博热搜" --with requests --with beautifulsoup4
    echo 安装完成！
) else if "%version%"=="2" (
    echo 正在安装微博热搜MCP服务(高级版)...
    python -m fastmcp install weibo_hotsearch_mcp_advanced.py --name "微博热搜高级版" --with requests --with beautifulsoup4
    echo 安装完成！
) else (
    echo 无效的选项，安装已取消。
)

pause
