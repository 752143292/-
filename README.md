# 李向前FIRE - 授权码生成器

消防调试类授权码生成工具

**🎯 现提供两个版本 / Two Versions Available:**
- 🔷 **C# 版本** - Windows Forms (仅 Windows)
- 🐍 **Python 版本** - tkinter (跨平台：Windows/Linux/macOS)

---

## ⚡ 一键启动 / One-Click Start

**最简单的运行方式 (推荐):**

| 操作系统 | 启动方式 |
|---------|---------|
| **Windows** | 双击 `start.bat` |
| **Linux/macOS** | 运行 `./start.sh` |
| **通用** | `python start.py` |

这些启动脚本会自动检查并安装所需依赖！  
These startup scripts will automatically check and install required dependencies!

❓ **遇到问题？** 查看 [故障排除指南.md](故障排除指南.md)

---

## 🐍 Python 版本（推荐 / Recommended）

### 快速开始 / Quick Start

**方法1: 使用启动脚本（推荐）**
```bash
# Windows: 双击 start.bat
# Linux/macOS: ./start.sh
# 或通用方式:
python start.py
```

**方法2: 手动运行**
```bash
# 1. 安装依赖 / Install dependencies
pip install -r requirements.txt

# 2. 运行程序 / Run program
python license_generator.py
```

### 特点 / Features
- ✅ **跨平台** - Windows / Linux / macOS
- ✅ **轻量级** - 源代码仅约 9KB
- ✅ **易修改** - Python 代码简单清晰
- ✅ **快速启动** - 无需编译，直接运行

📖 **详细教程** / Detailed Guide: [Python使用指南.md](Python使用指南.md)

---

## 🔷 C# 版本（Windows 专用）

### 快速开始 / Quick Start

```bash
# 编译运行 / Build and run
dotnet run

# 或打包为 EXE / Or package as EXE
dotnet publish LicenseGenerator.csproj -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -o ./output
```

### 特点 / Features
- ✅ **原生 Windows** - Windows Forms 界面
- ✅ **自包含** - 无需安装 .NET
- ✅ **单文件** - 打包为单个 EXE

📖 **详细教程** / Detailed Guide: [下载和运行指南.md](下载和运行指南.md)

---

## 📁 文件结构 / File Structure

### Python 版本 / Python Version
| 文件 / File | 说明 / Description | 大小 / Size |
|------------|-------------------|------------|
| `license_generator.py` | Python 主程序（完整实现）| ~9 KB |
| `requirements.txt` | Python 依赖包列表 | ~0.1 KB |

### C# 版本 / C# Version
| 文件 / File | 说明 / Description | 大小 / Size |
|------------|-------------------|------------|
| `Program.cs` | 程序入口 / Entry point | ~0.5 KB |
| `MainForm.cs` | 主窗体和所有逻辑 / Main form & logic | ~10 KB |
| `LicenseGenerator.csproj` | 项目配置 / Project config | ~0.4 KB |

---

## 📚 完整文档 / Complete Documentation

| 文档 | 说明 |
|------|------|
| 🐍 [Python使用指南.md](Python使用指南.md) | **Python 版本使用指南** |
| 📥 [下载和运行指南.md](下载和运行指南.md) | C# 版本使用指南 |
| 📖 [使用说明.md](使用说明.md) | 通用使用说明 |
| 📋 [功能说明.md](功能说明.md) | 功能详细说明 |
| ✅ [测试用例.md](测试用例.md) | 测试清单 |
| 🔧 [算法实现指南.md](算法实现指南.md) | 如何添加实际算法 |
| 📦 [项目交付说明.md](项目交付说明.md) | 项目总览 |
| 🖼️ [界面预览.md](界面预览.md) | 界面展示 |

---

## 🎯 功能特性 / Features

两个版本功能完全相同：

- ✅ 输入12位机器码（自动转大写）
- ✅ 生成授权码
- ✅ 一键复制授权码
- ✅ 实时显示时间
- ✅ 友好的错误提示
- ✅ 简洁的界面设计

---

## 💡 版本选择建议 / Version Selection Guide

### 选择 Python 版本，如果你 / Choose Python if:
- ✅ 需要跨平台运行 (Windows/Linux/macOS)
- ✅ 想要轻量级解决方案
- ✅ 熟悉 Python 或想快速修改代码
- ✅ 希望快速部署和分发

### 选择 C# 版本，如果你 / Choose C# if:
- ✅ 只在 Windows 上运行
- ✅ 喜欢原生 Windows 界面风格
- ✅ 熟悉 C# 和 .NET 生态
- ✅ 需要更好的 Windows 集成

---

## ⚠️ 注意事项 / Notes

**当前版本使用临时授权码算法**  
Current version uses temporary algorithm

- 输入：`ABC123DEF456`
- 输出：`TEMP-ABC123DE`

实际算法待实现，详见 [算法实现指南.md](算法实现指南.md)  
Actual algorithm to be implemented, see [算法实现指南.md](算法实现指南.md)

---

## 📊 版本对比 / Version Comparison

| 特性 | Python 版本 | C# 版本 |
|------|------------|---------|
| 平台支持 | Windows/Linux/macOS | 仅 Windows |
| 源代码大小 | ~9 KB (1个文件) | ~11 KB (3个文件) |
| 打包后大小 | ~15-30 MB | ~147 MB |
| 运行要求 | Python 3.7+ | 无（自包含） |
| 启动速度 | 快 | 非常快 |
| UI 框架 | tkinter | Windows Forms |
| 开发语言 | Python | C# |
| 易修改性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 跨平台 | ✅ | ❌ |
