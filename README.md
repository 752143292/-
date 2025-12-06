# 授权码生成器 - 李向前FIRE

消防调试类软件 - 授权码生成工具

## 功能说明

本软件用于生成授权码，具有以下功能：

1. **机器码输入**: 
   - 支持输入12位机器码
   - 自动转换为大写字母
   - 超过12位自动截断

2. **授权码生成**:
   - 根据机器码计算生成授权码
   - 授权码可直接复制到剪贴板

3. **界面特性**:
   - 显示当前时间（实时更新）
   - 简洁美观的图形界面
   - 中文界面，操作简单

## 使用方法

### 直接运行Python程序

1. 确保已安装Python 3.7或更高版本
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行程序：
   ```bash
   python authorization_app.py
   ```

### 生成Windows可执行文件（.exe）

1. 安装PyInstaller：
   ```bash
   pip install pyinstaller
   ```

2. 打包成exe：
   ```bash
   pyinstaller --onefile --windowed --name="李向前FIRE授权码生成器" authorization_app.py
   ```

3. 生成的exe文件位于 `dist` 目录下

### 高级打包选项（可选）

如果需要自定义图标或其他选项：

```bash
pyinstaller --onefile --windowed --name="李向前FIRE授权码生成器" --icon=app_icon.ico authorization_app.py
```

参数说明：
- `--onefile`: 打包成单个exe文件
- `--windowed`: 不显示控制台窗口（GUI程序）
- `--name`: 指定生成的exe文件名
- `--icon`: 指定程序图标（需要准备.ico文件）

## 注意事项

1. **授权码计算算法**: 
   - 当前代码中的 `calculate_auth_code()` 函数使用的是示例算法
   - 需要根据实际的计算规律更新该函数

2. **Python版本**: 
   - 推荐使用Python 3.7或更高版本
   - tkinter通常随Python一起安装

3. **Windows系统**: 
   - 生成的exe文件仅适用于Windows系统
   - 在其他操作系统上可直接运行Python程序

## 技术架构

- **编程语言**: Python 3
- **GUI框架**: tkinter (Python标准库)
- **打包工具**: PyInstaller

## 代码结构

```
authorization_app.py    # 主程序文件
├── AuthorizationApp   # 主应用程序类
│   ├── __init__()            # 初始化界面
│   ├── create_widgets()      # 创建GUI组件
│   ├── update_time()         # 更新时间显示
│   ├── on_machine_code_change()  # 处理机器码输入
│   ├── calculate_auth_code()     # 计算授权码（待实现）
│   ├── generate_auth_code()      # 生成授权码
│   ├── copy_auth_code()          # 复制授权码
│   └── clear_fields()            # 清空输入
└── main()             # 程序入口
```

## 开发者

李向前FIRE

## 更新日志

### v1.0 (初始版本)
- 实现基本GUI界面
- 机器码输入（12位限制、自动大写）
- 授权码显示和复制功能
- 实时时间显示
- 代码注释完善
