#!/bin/bash
# 李向前FIRE - 授权码生成器 Linux/macOS 启动脚本
# License Code Generator - Linux/macOS Startup Script

echo "============================================================"
echo "  李向前FIRE - 授权码生成器"
echo "  License Code Generator"
echo "============================================================"
echo ""

# 检查 Python 是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到 Python3"
    echo "❌ Error: Python3 not found"
    echo ""
    echo "请安装 Python 3.7 或更高版本"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

echo "✅ Python3 已安装"
echo ""

# 检查并安装依赖
echo "正在检查依赖... / Checking dependencies..."
python3 -c "import pyperclip" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "正在安装 pyperclip... / Installing pyperclip..."
    python3 -m pip install pyperclip
    if [ $? -ne 0 ]; then
        echo "❌ 安装失败 / Installation failed"
        exit 1
    fi
fi

echo "✅ 依赖已安装"
echo ""

# 启动程序
echo "============================================================"
echo "  正在启动程序... / Starting program..."
echo "============================================================"
echo ""

python3 license_generator.py

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ 程序运行出错 / Program error"
    read -p "按回车键退出 / Press Enter to exit..."
fi
