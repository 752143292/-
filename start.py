#!/usr/bin/env python3
"""
李向前FIRE - 授权码生成器 启动脚本
License Code Generator - Startup Script

这个脚本会自动检查依赖并启动程序
This script will automatically check dependencies and start the program
"""

import sys
import subprocess
import os

def check_python_version():
    """检查 Python 版本 / Check Python version"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ 错误: 需要 Python 3.7 或更高版本")
        print("❌ Error: Python 3.7 or higher required")
        print(f"   当前版本 / Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python 版本: {version.major}.{version.minor}.{version.micro}")
    return True

def check_and_install_dependencies():
    """检查并安装依赖 / Check and install dependencies"""
    try:
        import pyperclip
        print("✅ pyperclip 已安装 / pyperclip installed")
        return True
    except ImportError:
        print("⚠️  pyperclip 未安装，正在自动安装...")
        print("⚠️  pyperclip not installed, installing automatically...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyperclip"])
            print("✅ pyperclip 安装成功 / pyperclip installed successfully")
            return True
        except Exception as e:
            print(f"❌ 安装失败 / Installation failed: {e}")
            print("\n请手动运行 / Please run manually:")
            print(f"  {sys.executable} -m pip install pyperclip")
            return False

def check_tkinter():
    """检查 tkinter / Check tkinter"""
    try:
        import tkinter
        print("✅ tkinter 可用 / tkinter available")
        return True
    except ImportError:
        print("❌ tkinter 未安装 / tkinter not installed")
        print("\n安装方法 / Installation:")
        if sys.platform.startswith('linux'):
            print("  Ubuntu/Debian: sudo apt-get install python3-tk")
            print("  CentOS/RHEL: sudo yum install python3-tkinter")
        elif sys.platform == 'darwin':
            print("  macOS: brew install python-tk")
        else:
            print("  Windows: tkinter 应该已包含在 Python 安装中")
            print("  Windows: tkinter should be included in Python installation")
        return False

def main():
    """主函数 / Main function"""
    print("=" * 60)
    print("  李向前FIRE - 授权码生成器")
    print("  License Code Generator")
    print("=" * 60)
    print()
    
    # 检查 Python 版本
    if not check_python_version():
        input("\n按回车键退出 / Press Enter to exit...")
        sys.exit(1)
    
    print()
    
    # 检查 tkinter
    if not check_tkinter():
        input("\n按回车键退出 / Press Enter to exit...")
        sys.exit(1)
    
    print()
    
    # 检查并安装依赖
    if not check_and_install_dependencies():
        input("\n按回车键退出 / Press Enter to exit...")
        sys.exit(1)
    
    print()
    print("=" * 60)
    print("  正在启动程序... / Starting program...")
    print("=" * 60)
    print()
    
    # 导入并运行主程序
    try:
        import license_generator
        license_generator.main()
    except Exception as e:
        print(f"❌ 启动失败 / Startup failed: {e}")
        import traceback
        traceback.print_exc()
        input("\n按回车键退出 / Press Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()
