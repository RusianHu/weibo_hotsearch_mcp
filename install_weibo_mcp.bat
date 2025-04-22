@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo 微博热搜MCP服务安装脚本
echo ============================

:: 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到Python，请先安装Python 3.10或更高版本。
    pause
    exit /b 1
)

:: 检查fastmcp是否安装
python -c "import fastmcp" >nul 2>&1
if %errorlevel% neq 0 (
    echo [警告] 未检测到fastmcp包，是否立即安装？(Y/N)
    set /p install_fastmcp=
    if /i "!install_fastmcp!"=="Y" (
        echo 正在安装fastmcp...
        python -m pip install fastmcp --proxy socks5://127.0.0.1:10808
        if %errorlevel% neq 0 (
            echo [错误] 安装fastmcp失败，请检查网络连接或手动安装。
            pause
            exit /b 1
        )
    ) else (
        echo 已取消安装。
        pause
        exit /b 1
    )
)

echo 请选择要安装的版本:
echo 1. 基础版
echo 2. 高级版
echo ============================

set /p version=请输入选项(1或2):

:: 询问是否需要设置Cookie
echo.
echo 是否需要设置微博Cookie？(Y/N)
echo 设置Cookie可以提高获取数据的稳定性和准确性。
set /p set_cookie=

set COOKIE_PARAM=""
if /i "%set_cookie%"=="Y" (
    echo.
    echo 请输入微博Cookie (如不清楚如何获取，请直接按回车跳过):
    set /p weibo_cookie=
    if not "!weibo_cookie!"=="" (
        set "COOKIE_PARAM=--env WEIBO_COOKIE=!weibo_cookie!"
    )
)

if "%version%"=="1" (
    echo 正在安装微博热搜MCP服务(基础版)...
    python -m fastmcp install weibo_hotsearch_mcp.py --name "微博热搜" --with requests --with beautifulsoup4 %COOKIE_PARAM%
    if %errorlevel% neq 0 (
        echo [错误] 安装失败，请检查错误信息。
    ) else (
        echo 安装完成！
    )
) else if "%version%"=="2" (
    echo 正在安装微博热搜MCP服务(高级版)...
    python -m fastmcp install weibo_hotsearch_mcp_advanced.py --name "微博热搜高级版" --with requests --with beautifulsoup4 %COOKIE_PARAM%
    if %errorlevel% neq 0 (
        echo [错误] 安装失败，请检查错误信息。
    ) else (
        echo 安装完成！
    )
) else (
    echo 无效的选项，安装已取消。
)

endlocal
pause
