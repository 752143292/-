@echo off
REM 授权码生成器构建脚本
REM 用于将Python程序打包成Windows可执行文件

echo ========================================
echo 李向前FIRE授权码生成器 - 构建脚本
echo ========================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未找到Python，请先安装Python 3.7或更高版本
    pause
    exit /b 1
)

echo [1/3] 检查并安装依赖...
pip install pyinstaller
if errorlevel 1 (
    echo [错误] 安装PyInstaller失败
    pause
    exit /b 1
)

echo.
echo [2/3] 打包程序为exe文件...
pyinstaller --onefile --windowed --name="李向前FIRE授权码生成器" authorization_app.py
if errorlevel 1 (
    echo [错误] 打包失败
    pause
    exit /b 1
)

echo.
echo [3/3] 清理临时文件...
REM 保留dist目录和exe文件，删除其他临时文件
if exist "build" rmdir /s /q "build"
if exist "*.spec" del /q "*.spec"

echo.
echo ========================================
echo 构建完成！
echo 生成的exe文件位于: dist\李向前FIRE授权码生成器.exe
echo ========================================
echo.

pause
