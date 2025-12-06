# 李向前FIRE - 授权码生成器

消防调试类授权码生成工具

## 📥 如何获取程序 / How to Get the Program

### 方法1：一键编译（最快）/ Method 1: One-Command Build (Fastest)

```bash
# 需要安装 .NET 8.0 SDK
# Requires .NET 8.0 SDK
dotnet publish LicenseGenerator.csproj -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -o ./output
```

编译完成后运行：`output/LicenseGenerator.exe`  
After building, run: `output/LicenseGenerator.exe`

### 方法2：复制源代码直接运行 / Method 2: Copy Source Code and Run

1. 复制以下3个文件：  
   Copy these 3 files:
   - `Program.cs`
   - `MainForm.cs`
   - `LicenseGenerator.csproj`

2. 在文件夹中运行：  
   Run in the folder:
   ```bash
   dotnet run
   ```

📖 **详细教程** / Detailed Guide: [下载和运行指南.md](下载和运行指南.md)

## 💻 源代码 / Source Code

所有源代码可直接查看和复制（仅3个文件，共约11KB）：  
All source code is available for viewing and copying (only 3 files, ~11KB total):

| 文件 / File | 说明 / Description | 大小 / Size |
|------------|-------------------|------------|
| `Program.cs` | 程序入口 / Entry point | ~0.5 KB |
| `MainForm.cs` | 主窗体和所有逻辑 / Main form & logic | ~10 KB |
| `LicenseGenerator.csproj` | 项目配置 / Project config | ~0.4 KB |

**特点 / Features:**
- ✅ 代码简洁清晰，易于理解
- ✅ 中英文双语注释
- ✅ 无外部依赖，只需 .NET 8.0

## 📚 文档 / Documentation

| 文档 | 说明 |
|------|------|
| 📥 [下载和运行指南.md](下载和运行指南.md) | **如何获取和运行程序** |
| 📖 [使用说明.md](使用说明.md) | 详细使用指南 |
| 📋 [功能说明.md](功能说明.md) | 功能详细说明 |
| ✅ [测试用例.md](测试用例.md) | 测试清单 |
| 🔧 [算法实现指南.md](算法实现指南.md) | 如何添加实际算法 |
| 📦 [项目交付说明.md](项目交付说明.md) | 项目总览 |
| 🖼️ [界面预览.md](界面预览.md) | 界面展示 |

## ⚡ 快速开始 / Quick Start

1. **克隆仓库** / Clone repository
   ```bash
   git clone [仓库地址]
   cd [仓库目录]
   ```

2. **编译运行** / Build and run
   ```bash
   dotnet run
   ```

## 🎯 功能特性 / Features

- ✅ 输入12位机器码（自动转大写）
- ✅ 生成授权码
- ✅ 一键复制授权码
- ✅ 实时显示时间
- ✅ 友好的错误提示
- ✅ 简洁的界面设计

## 💡 系统要求 / System Requirements

**开发/编译 / Development:**
- .NET 8.0 SDK
- Windows、Linux 或 macOS

**运行 / Runtime:**
- Windows 7 或更高版本
- 64位系统
- 编译后的程序自包含，无需安装 .NET

## ⚠️ 注意事项 / Notes

当前版本使用临时授权码算法（`TEMP-` + 前8位机器码）  
实际算法待实现，详见 [算法实现指南.md](算法实现指南.md)

Current version uses temporary algorithm (`TEMP-` + first 8 chars)  
Actual algorithm to be implemented, see [算法实现指南.md](算法实现指南.md)
