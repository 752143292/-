# 快速开始 / Quick Start

## 中文版

### 🚀 立即试运行

**最简单的方法（推荐首次测试）：**

```bash
# 1. 进入项目目录
cd /path/to/project

# 2. 直接运行程序
python authorization_app.py
```

或者在Windows系统上：
```bash
python authorization_app.py
```

**程序将会打开，您可以立即开始测试！**

### 📋 使用步骤

1. **输入机器码**：在第一个输入框输入12位机器码（会自动转大写）
2. **生成授权码**：点击蓝色"生成授权码"按钮
3. **复制授权码**：点击绿色"复制授权码"按钮复制到剪贴板
4. **清空重试**：点击红色"清空"按钮清除所有内容

### 🎯 测试示例

试试这些机器码：
- `abc123def456` → 自动转换为 `ABC123DEF456`
- `123456789012` → 直接使用
- `xyz999abc111` → 自动转换为 `XYZ999ABC111`

### 📦 生成EXE文件

**Windows用户：**
```bash
# 双击运行
build.bat

# 或在命令行运行
build.bat
```

**Linux/Mac用户：**
```bash
chmod +x build.sh
./build.sh
```

生成的exe文件位于 `dist` 目录下。

### ⚙️ 添加您的计算规律

**重要：** 当前程序使用的是示例计算公式，请按以下步骤添加您的实际计算规律：

1. 打开 `authorization_app.py`
2. 找到 `calculate_auth_code()` 函数（约207行）
3. 在标注 `TODO` 的地方替换为您的计算逻辑
4. 保存并重新运行测试

**需要帮助？** 查看 `DEVELOPER_GUIDE.md` 获取详细说明和示例代码。

### 📚 更多文档

- **完整使用指南**：`USAGE_GUIDE.md`
- **开发者指南**：`DEVELOPER_GUIDE.md`
- **界面说明**：`UI_DESCRIPTION.md`
- **项目说明**：`README.md`

---

## English Version

### 🚀 Run Immediately

**The Simplest Way (Recommended for First Test):**

```bash
# 1. Navigate to project directory
cd /path/to/project

# 2. Run the program directly
python authorization_app.py
```

Or on Windows:
```bash
python authorization_app.py
```

**The program window will open and you can start testing immediately!**

### 📋 Usage Steps

1. **Enter Machine Code**: Input 12-character machine code in the first box (auto-converts to uppercase)
2. **Generate Auth Code**: Click the blue "Generate Authorization Code" button
3. **Copy Auth Code**: Click the green "Copy Authorization Code" button to copy to clipboard
4. **Clear and Retry**: Click the red "Clear" button to reset

### 🎯 Test Examples

Try these machine codes:
- `abc123def456` → Auto-converts to `ABC123DEF456`
- `123456789012` → Used directly
- `xyz999abc111` → Auto-converts to `XYZ999ABC111`

### 📦 Build EXE File

**Windows Users:**
```bash
# Double-click to run
build.bat

# Or run in command line
build.bat
```

**Linux/Mac Users:**
```bash
chmod +x build.sh
./build.sh
```

The generated exe file is located in the `dist` directory.

### ⚙️ Add Your Calculation Algorithm

**Important:** The program currently uses a sample calculation formula. Follow these steps to add your actual calculation logic:

1. Open `authorization_app.py`
2. Find the `calculate_auth_code()` function (around line 207)
3. Replace the placeholder marked with `TODO` with your calculation logic
4. Save and re-run to test

**Need Help?** See `DEVELOPER_GUIDE.md` for detailed instructions and example code.

### 📚 More Documentation

- **Complete Usage Guide**: `USAGE_GUIDE.md`
- **Developer Guide**: `DEVELOPER_GUIDE.md`
- **UI Description**: `UI_DESCRIPTION.md`
- **Project README**: `README.md`

---

## System Requirements / 系统要求

- **Python**: 3.7 or higher / 3.7或更高版本
- **OS**: Windows, Linux, or Mac / Windows、Linux或Mac系统
- **Dependencies**: tkinter (usually included with Python) / tkinter（通常随Python安装）

## File Structure / 文件结构

```
project/
├── authorization_app.py      # Main application / 主程序
├── requirements.txt           # Python dependencies / Python依赖
├── build.bat                  # Windows build script / Windows构建脚本
├── build.sh                   # Linux/Mac build script / Linux/Mac构建脚本
├── test_authorization.py      # Unit tests / 单元测试
├── README.md                  # Project overview / 项目概述
├── USAGE_GUIDE.md            # Usage guide / 使用指南
├── DEVELOPER_GUIDE.md        # Developer guide / 开发者指南
├── UI_DESCRIPTION.md         # UI description / 界面说明
└── QUICK_START.md            # This file / 本文件
```

## Troubleshooting / 故障排除

### Problem: "No module named tkinter"
**Solution:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Mac (usually pre-installed)
brew install python-tk
```

### Problem: Build fails / 构建失败
**Solution:**
```bash
# Install PyInstaller manually
pip install pyinstaller

# Then run build script again
```

### Problem: Program doesn't start / 程序无法启动
**Solution:**
- Make sure Python 3.7+ is installed / 确保安装了Python 3.7+
- Check if tkinter is available / 检查tkinter是否可用
- Run in terminal to see error messages / 在终端运行查看错误信息

---

**版本 / Version:** 1.0  
**最后更新 / Last Updated:** 2025-12-06
