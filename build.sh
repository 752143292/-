#!/bin/bash
# 授权码生成器构建脚本（Linux/Mac版本）
# 用于将Python程序打包成可执行文件

echo "========================================"
echo "李向前FIRE授权码生成器 - 构建脚本"
echo "========================================"
echo ""

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "[错误] 未找到Python3，请先安装Python 3.7或更高版本"
    exit 1
fi

echo "[1/3] 检查并安装依赖..."
pip3 install pyinstaller
if [ $? -ne 0 ]; then
    echo "[错误] 安装PyInstaller失败"
    exit 1
fi

echo ""
echo "[2/3] 打包程序..."
pyinstaller --onefile --windowed --name="李向前FIRE授权码生成器" authorization_app.py
if [ $? -ne 0 ]; then
    echo "[错误] 打包失败"
    exit 1
fi

echo ""
echo "[3/3] 清理临时文件..."
# 保留dist目录，删除其他临时文件
rm -rf build
rm -f *.spec

echo ""
echo "========================================"
echo "构建完成！"
echo "生成的文件位于: dist/李向前FIRE授权码生成器"
echo "========================================"
echo ""
