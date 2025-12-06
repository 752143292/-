"""
李向前FIRE - 授权码生成器
License Code Generator

主程序文件 - 使用 tkinter 创建图形界面
Main program file - Uses tkinter to create GUI
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import pyperclip


class LicenseGeneratorApp:
    """
    主应用程序类 - 授权码生成器
    Main Application Class - License Code Generator
    """
    
    def __init__(self, root):
        """
        初始化应用程序
        Initialize application
        
        Args:
            root: tkinter 根窗口 / tkinter root window
        """
        self.root = root
        self.setup_window()
        self.create_widgets()
        self.update_time()
    
    def setup_window(self):
        """
        配置主窗口属性
        Configure main window properties
        """
        # 窗口标题 / Window title
        self.root.title("李向前FIRE - 授权码生成器")
        
        # 窗口大小 / Window size
        self.root.geometry("500x400")
        
        # 禁止调整窗口大小 / Disable window resizing
        self.root.resizable(False, False)
        
        # 窗口居中显示 / Center window on screen
        self.center_window()
    
    def center_window(self):
        """
        将窗口居中显示在屏幕上
        Center the window on the screen
        """
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """
        创建所有UI组件
        Create all UI components
        """
        # 标题标签 / Title label
        self.lbl_title = tk.Label(
            self.root,
            text="李向前FIRE",
            font=("Microsoft YaHei", 18, "bold")
        )
        self.lbl_title.pack(pady=(20, 5))
        
        # 时间显示标签 / Time display label
        self.lbl_time = tk.Label(
            self.root,
            text="",
            font=("Microsoft YaHei", 10),
            fg="darkblue"
        )
        self.lbl_time.pack(pady=(0, 20))
        
        # 机器码输入区域 / Machine code input area
        self.create_machine_code_section()
        
        # 授权码显示区域 / Authorization code display area
        self.create_auth_code_section()
        
        # 按钮区域 / Button area
        self.create_buttons()
    
    def create_machine_code_section(self):
        """
        创建机器码输入区域
        Create machine code input section
        """
        # 机器码标签 / Machine code label
        lbl_machine_code = tk.Label(
            self.root,
            text="机器码 (12位):",
            font=("Microsoft YaHei", 10)
        )
        lbl_machine_code.pack(anchor='w', padx=30, pady=(10, 5))
        
        # 机器码输入框 / Machine code input box
        self.txt_machine_code = tk.Entry(
            self.root,
            font=("Consolas", 12),
            width=42
        )
        self.txt_machine_code.pack(padx=30, pady=(0, 10))
        
        # 绑定输入事件，限制长度和转大写 / Bind input event for length limit and uppercase
        self.txt_machine_code.bind('<KeyRelease>', self.on_machine_code_changed)
    
    def create_auth_code_section(self):
        """
        创建授权码显示区域
        Create authorization code display section
        """
        # 授权码标签 / Authorization code label
        lbl_auth_code = tk.Label(
            self.root,
            text="授权码:",
            font=("Microsoft YaHei", 10)
        )
        lbl_auth_code.pack(anchor='w', padx=30, pady=(10, 5))
        
        # 授权码显示框（只读）/ Authorization code display box (read-only)
        self.txt_auth_code = tk.Entry(
            self.root,
            font=("Consolas", 12),
            width=42,
            state='readonly',
            readonlybackground='lightgray'
        )
        self.txt_auth_code.pack(padx=30, pady=(0, 20))
    
    def create_buttons(self):
        """
        创建按钮区域
        Create button area
        """
        # 按钮容器框架 / Button container frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        # 生成授权码按钮 / Generate authorization code button
        self.btn_generate = tk.Button(
            button_frame,
            text="生成授权码",
            font=("Microsoft YaHei", 10),
            width=18,
            height=2,
            command=self.generate_auth_code
        )
        self.btn_generate.pack(side='left', padx=10)
        
        # 复制授权码按钮 / Copy authorization code button
        self.btn_copy = tk.Button(
            button_frame,
            text="复制授权码",
            font=("Microsoft YaHei", 10),
            width=18,
            height=2,
            command=self.copy_auth_code
        )
        self.btn_copy.pack(side='left', padx=10)
    
    def on_machine_code_changed(self, event):
        """
        机器码输入框内容改变事件处理
        Handle machine code input box content change event
        
        Args:
            event: 键盘事件 / Keyboard event
        """
        # 获取当前输入 / Get current input
        current_text = self.txt_machine_code.get()
        
        # 转换为大写 / Convert to uppercase
        upper_text = current_text.upper()
        
        # 限制长度为12位 / Limit length to 12 characters
        if len(upper_text) > 12:
            upper_text = upper_text[:12]
        
        # 如果有变化，更新输入框 / Update input box if changed
        if current_text != upper_text:
            # 保存光标位置 / Save cursor position
            cursor_position = self.txt_machine_code.index(tk.INSERT)
            
            # 更新文本 / Update text
            self.txt_machine_code.delete(0, tk.END)
            self.txt_machine_code.insert(0, upper_text)
            
            # 恢复光标位置 / Restore cursor position
            self.txt_machine_code.icursor(min(cursor_position, len(upper_text)))
    
    def generate_auth_code(self):
        """
        生成授权码按钮点击事件处理
        Handle generate authorization code button click event
        """
        # 获取机器码 / Get machine code
        machine_code = self.txt_machine_code.get().strip()
        
        # 验证机器码是否输入 / Validate if machine code is entered
        if not machine_code:
            messagebox.showwarning("提示", "请输入机器码！")
            return
        
        # 验证机器码长度 / Validate machine code length
        if len(machine_code) != 12:
            messagebox.showwarning("提示", "机器码必须为12位！")
            return
        
        # 计算授权码 / Calculate authorization code
        auth_code = self.calculate_authorization_code(machine_code)
        
        # 显示授权码 / Display authorization code
        self.txt_auth_code.config(state='normal')
        self.txt_auth_code.delete(0, tk.END)
        self.txt_auth_code.insert(0, auth_code)
        self.txt_auth_code.config(state='readonly')
    
    def calculate_authorization_code(self, machine_code):
        """
        计算授权码的方法 - 待实现具体算法
        Calculate authorization code method - Algorithm to be implemented
        
        Args:
            machine_code: 机器码 / Machine code
            
        Returns:
            授权码 / Authorization code
        """
        # TODO: 在这里实现具体的授权码计算逻辑
        # TODO: Implement specific authorization code calculation logic here
        
        # 验证输入 / Validate input
        if not machine_code or len(machine_code) < 8:
            return "ERROR-INVALID"
        
        # 目前返回一个占位符，等待后续添加实际计算规律
        # Currently returns a placeholder, waiting for actual calculation pattern to be added
        
        # 临时实现：简单的示例计算（这将被实际算法替换）
        # Temporary implementation: simple example calculation (this will be replaced with actual algorithm)
        return "TEMP-" + machine_code[:8]
    
    def copy_auth_code(self):
        """
        复制授权码按钮点击事件处理
        Handle copy authorization code button click event
        """
        # 获取授权码 / Get authorization code
        auth_code = self.txt_auth_code.get().strip()
        
        # 验证授权码是否已生成 / Validate if authorization code has been generated
        if not auth_code:
            messagebox.showwarning("提示", "请先生成授权码！")
            return
        
        # 复制到剪贴板 / Copy to clipboard
        try:
            pyperclip.copy(auth_code)
            messagebox.showinfo("成功", "授权码已复制到剪贴板！")
        except Exception as e:
            messagebox.showerror("错误", f"复制失败: {str(e)}")
    
    def update_time(self):
        """
        更新时间显示
        Update time display
        """
        # 获取当前时间 / Get current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 更新时间标签 / Update time label
        self.lbl_time.config(text=current_time)
        
        # 每秒更新一次 / Update every second
        self.root.after(1000, self.update_time)


def main():
    """
    程序入口点
    Program entry point
    """
    # 创建主窗口 / Create main window
    root = tk.Tk()
    
    # 创建应用程序实例 / Create application instance
    app = LicenseGeneratorApp(root)
    
    # 运行主循环 / Run main loop
    root.mainloop()


if __name__ == "__main__":
    main()
