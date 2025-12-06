@echo off
REM 李向前FIRE - 授权码生成器 Windows 启动脚本
REM License Code Generator - Windows Startup Script

echo ============================================================
echo   李向前FIRE - 授权码生成器
echo   License Code Generator
echo ============================================================
echo.

REM 检查 Python 是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo X 错误: 未找到 Python
    echo X Error: Python not found
    echo.
    echo 请从以下地址下载并安装 Python 3.7 或更高版本:
    echo Please download and install Python 3.7 or higher from:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [32m√ Python 已安装[0m
echo.

REM 检查并安装依赖
echo 正在检查依赖... / Checking dependencies...
python -c "import pyperclip" >nul 2>&1
if errorlevel 1 (
    echo 正在安装 pyperclip... / Installing pyperclip...
    python -m pip install pyperclip
    if errorlevel 1 (
        echo X 安装失败 / Installation failed
        pause
        exit /b 1
    )
)

echo [32m√ 依赖已安装[0m
echo.

REM 启动程序
echo ============================================================
echo   正在启动程序... / Starting program...
echo ============================================================
echo.

python license_generator.py

if errorlevel 1 (
    echo.
    echo X 程序运行出错 / Program error
    pause
)
