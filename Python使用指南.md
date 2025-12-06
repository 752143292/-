# Python 版本使用指南 / Python Version Usage Guide

## 李向前FIRE - 授权码生成器 (Python版)

基于 Python 和 tkinter 的跨平台授权码生成工具。  
Cross-platform license code generator based on Python and tkinter.

---

## 快速开始 / Quick Start

### 方法1：直接运行（推荐）/ Method 1: Direct Run (Recommended)

```bash
# 1. 安装依赖 / Install dependencies
pip install -r requirements.txt

# 2. 运行程序 / Run program
python license_generator.py
```

### 方法2：创建可执行文件 / Method 2: Create Executable

```bash
# 安装 PyInstaller
pip install pyinstaller

# 创建单文件可执行程序
pyinstaller --onefile --windowed --name "李向前FIRE授权码生成器" license_generator.py

# 可执行文件位于 / Executable located at:
# dist/李向前FIRE授权码生成器.exe (Windows)
# dist/李向前FIRE授权码生成器 (Linux/macOS)
```

---

## 系统要求 / System Requirements

### 基本要求 / Basic Requirements
- **Python**: 3.7 或更高版本 / 3.7 or higher
- **操作系统 / OS**: Windows / Linux / macOS (跨平台 / cross-platform)

### Python 依赖包 / Python Dependencies
- `tkinter` - GUI 库（Python 自带 / Built-in with Python）
- `pyperclip` - 剪贴板操作 / Clipboard operations

---

## 安装步骤 / Installation Steps

### 1. 安装 Python
如果还没有安装 Python，请从官网下载：  
If you haven't installed Python, download from official website:

**Windows**: https://www.python.org/downloads/  
**Linux**: 通常已预装 / Usually pre-installed
```bash
sudo apt-get install python3 python3-pip python3-tk  # Ubuntu/Debian
```
**macOS**: 
```bash
brew install python3
```

### 2. 安装依赖包
```bash
pip install -r requirements.txt
```

或者手动安装 / Or install manually:
```bash
pip install pyperclip
```

### 3. 运行程序
```bash
python license_generator.py
```

---

## 文件说明 / File Description

```
/
├── license_generator.py    # Python 主程序文件（单文件实现）
├── requirements.txt        # Python 依赖包列表
└── Python使用指南.md        # 本文件
```

### license_generator.py (约 9KB)
包含完整的应用程序代码：
- 图形界面实现（tkinter）
- 机器码输入处理（12位，自动转大写）
- 授权码生成逻辑（占位符算法）
- 剪贴板复制功能
- 实时时间显示

---

## 功能特性 / Features

✅ **跨平台** - Windows / Linux / macOS 都可运行  
✅ **单文件** - 只需一个 Python 文件  
✅ **轻量级** - 源代码仅约 9KB  
✅ **无需编译** - 直接运行 Python 脚本  
✅ **易于分发** - 可打包成独立可执行文件  

### 界面功能 / UI Features
- ✅ 输入12位机器码（自动转大写）
- ✅ 生成授权码（点击"生成授权码"按钮）
- ✅ 复制授权码（点击"复制授权码"按钮）
- ✅ 实时显示当前时间（每秒更新）
- ✅ 友好的错误提示
- ✅ 简洁的界面设计

---

## 打包为可执行文件 / Package as Executable

### Windows

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包为单个 .exe 文件
pyinstaller --onefile --windowed --icon=icon.ico --name "LicenseGenerator" license_generator.py

# 输出文件 / Output file:
# dist/LicenseGenerator.exe
```

### Linux

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包
pyinstaller --onefile --windowed --name "LicenseGenerator" license_generator.py

# 输出文件 / Output file:
# dist/LicenseGenerator
```

### macOS

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包为 .app
pyinstaller --onefile --windowed --name "LicenseGenerator" license_generator.py

# 输出文件 / Output file:
# dist/LicenseGenerator.app
```

---

## 算法实现 / Algorithm Implementation

当前使用临时算法：`TEMP-` + 机器码前8位  
Current temporary algorithm: `TEMP-` + first 8 chars of machine code

### 如何修改算法 / How to Modify Algorithm

在 `license_generator.py` 文件中找到 `calculate_authorization_code` 方法：

```python
def calculate_authorization_code(self, machine_code):
    """
    计算授权码的方法 - 待实现具体算法
    Calculate authorization code method - Algorithm to be implemented
    """
    # 验证输入
    if not machine_code or len(machine_code) < 8:
        return "ERROR-INVALID"
    
    # TODO: 在这里实现具体的授权码计算逻辑
    # 临时实现
    return "TEMP-" + machine_code[:8]
    
    # ========================================
    # 在这里添加你的实际算法
    # Add your actual algorithm here
    # ========================================
```

---

## 使用示例 / Usage Example

### 测试用例 / Test Cases

| 输入机器码 | 输出授权码（临时） |
|-----------|------------------|
| ABC123DEF456 | TEMP-ABC123DE |
| XYZ789UVW012 | TEMP-XYZ789UV |
| abc123def456 | TEMP-ABC123DE |

---

## 常见问题 / FAQ

### Q: 为什么选择 Python 版本？
**A**: 
- ✅ 跨平台：可在 Windows、Linux、macOS 运行
- ✅ 轻量级：源代码仅约 9KB，无需大量依赖
- ✅ 易修改：代码简单清晰，易于理解和修改
- ✅ 快速开发：Python 开发效率高

### Q: Python 版本和 C# 版本有什么区别？
**A**:

| 特性 | C# 版本 | Python 版本 |
|------|---------|------------|
| 平台 | 仅 Windows | Windows/Linux/macOS |
| 文件大小 | 约 147MB | 约 9KB (源码) |
| 运行要求 | 无需 .NET | 需要 Python |
| 打包后大小 | 约 155MB | 约 15-30MB |
| 开发语言 | C# | Python |
| UI 框架 | Windows Forms | tkinter |

### Q: 如何在没有 Python 的电脑上运行？
**A**: 使用 PyInstaller 打包成独立可执行文件，打包后的程序可以在没有 Python 的电脑上运行。

### Q: tkinter 在 Linux 上显示不正常怎么办？
**A**: 确保安装了 `python3-tk` 包：
```bash
sudo apt-get install python3-tk  # Ubuntu/Debian
sudo yum install python3-tkinter  # CentOS/RHEL
```

### Q: 剪贴板功能在 Linux 上不工作？
**A**: 安装必要的剪贴板工具：
```bash
sudo apt-get install xclip  # 或 xsel
```

---

## 与 C# 版本对比 / Comparison with C# Version

### 优势 / Advantages
- ✅ **跨平台** - 可在多个操作系统运行
- ✅ **体积小** - 源代码仅约 9KB
- ✅ **易修改** - Python 语法简单，易于学习
- ✅ **快速迭代** - 无需编译，即改即用

### 劣势 / Disadvantages
- ❌ **运行依赖** - 需要安装 Python 环境（可通过打包解决）
- ❌ **界面风格** - tkinter 界面较为朴素（可使用 PyQt5 等库改进）
- ❌ **启动速度** - 可能略慢于 C# 版本

---

## 技术支持 / Technical Support

相关文档：
- 📖 [功能说明.md](功能说明.md) - 功能详细说明
- 📋 [测试用例.md](测试用例.md) - 测试清单
- 🔧 [算法实现指南.md](算法实现指南.md) - 算法实现指南

---

## 版本信息 / Version Information

- **版本 / Version**: 1.0 (Python)
- **Python 要求 / Python Required**: 3.7+
- **依赖包 / Dependencies**: pyperclip
- **UI 框架 / UI Framework**: tkinter

---

**注意 / Note**: 
两个版本（C# 和 Python）功能完全相同，可以根据需要选择使用。  
Both versions (C# and Python) have identical functionality, choose based on your needs.
