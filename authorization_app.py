#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
授权码生成器 - Authorization Code Generator
作者: 李向前FIRE
功能: 根据机器码生成授权码
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading


class AuthorizationApp:
    """授权码生成器主应用程序类"""
    
    def __init__(self, root):
        """
        初始化应用程序
        
        Args:
            root: tkinter主窗口对象
        """
        self.root = root
        self.root.title("李向前FIRE")  # 设置窗口标题
        self.root.geometry("500x400")  # 设置窗口大小
        self.root.resizable(False, False)  # 禁止调整窗口大小
        
        # 创建界面组件
        self.create_widgets()
        
        # 启动时间更新线程
        self.update_time()
        
    def create_widgets(self):
        """创建所有界面组件"""
        
        # ==================== 标题区域 ====================
        # 标题框架
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        title_frame.pack(fill=tk.X, pady=(0, 10))
        title_frame.pack_propagate(False)
        
        # 应用标题
        title_label = tk.Label(
            title_frame,
            text="李向前FIRE - 授权码生成器",
            font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(pady=(10, 5))
        
        # 时间显示标签
        self.time_label = tk.Label(
            title_frame,
            text="",
            font=("Arial", 10),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        self.time_label.pack()
        
        # ==================== 主内容区域 ====================
        # 主内容框架
        main_frame = tk.Frame(self.root, padx=30, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # ---------- 机器码输入区域 ----------
        # 机器码标签
        machine_code_label = tk.Label(
            main_frame,
            text="机器码 (12位):",
            font=("Arial", 12, "bold")
        )
        machine_code_label.pack(anchor=tk.W, pady=(0, 5))
        
        # 机器码输入框
        self.machine_code_entry = tk.Entry(
            main_frame,
            font=("Arial", 14),
            width=30,
            justify=tk.CENTER
        )
        self.machine_code_entry.pack(pady=(0, 5))
        
        # 绑定输入事件，实现大写转换和长度限制
        self.machine_code_entry.bind('<KeyRelease>', self.on_machine_code_change)
        
        # 提示信息
        hint_label = tk.Label(
            main_frame,
            text="* 自动转换为大写，最多12位字符",
            font=("Arial", 9),
            fg="gray"
        )
        hint_label.pack(anchor=tk.W, pady=(0, 20))
        
        # ---------- 授权码显示区域 ----------
        # 授权码标签
        auth_code_label = tk.Label(
            main_frame,
            text="授权码:",
            font=("Arial", 12, "bold")
        )
        auth_code_label.pack(anchor=tk.W, pady=(0, 5))
        
        # 授权码显示框（只读）
        self.auth_code_entry = tk.Entry(
            main_frame,
            font=("Arial", 14),
            width=30,
            justify=tk.CENTER,
            state='readonly',  # 设置为只读
            readonlybackground="white"
        )
        self.auth_code_entry.pack(pady=(0, 10))
        
        # ---------- 按钮区域 ----------
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        # 生成授权码按钮
        generate_btn = tk.Button(
            button_frame,
            text="生成授权码",
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            width=12,
            height=1,
            cursor="hand2",
            command=self.generate_auth_code
        )
        generate_btn.pack(side=tk.LEFT, padx=5)
        
        # 复制授权码按钮
        copy_btn = tk.Button(
            button_frame,
            text="复制授权码",
            font=("Arial", 12, "bold"),
            bg="#2ecc71",
            fg="white",
            width=12,
            height=1,
            cursor="hand2",
            command=self.copy_auth_code
        )
        copy_btn.pack(side=tk.LEFT, padx=5)
        
        # 清空按钮
        clear_btn = tk.Button(
            button_frame,
            text="清空",
            font=("Arial", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            width=12,
            height=1,
            cursor="hand2",
            command=self.clear_fields
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
    def update_time(self):
        """更新时间显示（每秒更新一次）"""
        current_time = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
        self.time_label.config(text=f"当前时间: {current_time}")
        # 每1000毫秒（1秒）后再次调用此函数
        self.root.after(1000, self.update_time)
        
    def on_machine_code_change(self, event):
        """
        机器码输入框内容变化时的处理函数
        实现自动转换为大写和12位长度限制
        
        Args:
            event: 键盘事件对象
        """
        # 获取当前输入内容
        current_value = self.machine_code_entry.get()
        
        # 转换为大写
        upper_value = current_value.upper()
        
        # 限制为12位
        if len(upper_value) > 12:
            upper_value = upper_value[:12]
            
        # 如果内容发生了变化，更新输入框
        if upper_value != current_value:
            # 保存当前光标位置
            cursor_position = self.machine_code_entry.index(tk.INSERT)
            # 更新内容
            self.machine_code_entry.delete(0, tk.END)
            self.machine_code_entry.insert(0, upper_value)
            # 恢复光标位置（考虑长度限制）
            new_position = min(cursor_position, len(upper_value))
            self.machine_code_entry.icursor(new_position)
            
    def calculate_auth_code(self, machine_code):
        """
        计算授权码的函数（待实现具体算法）
        
        Args:
            machine_code: 输入的机器码字符串
            
        Returns:
            str: 计算得出的授权码
            
        注意: 此处为占位函数，具体计算规律需要根据实际需求实现
        """
        # ============================================
        # TODO: 在此处添加授权码计算逻辑
        # 当前返回的是示例授权码，需要替换为实际算法
        # ============================================
        
        if not machine_code:
            return ""
            
        # 临时示例：简单处理（实际使用时需替换）
        # 这里只是一个占位符，展示返回格式
        example_auth_code = f"AUTH-{machine_code}-DEMO"
        
        return example_auth_code
        
    def generate_auth_code(self):
        """生成授权码按钮的处理函数"""
        # 获取机器码输入
        machine_code = self.machine_code_entry.get().strip()
        
        # 验证机器码
        if not machine_code:
            messagebox.showwarning("警告", "请输入机器码！")
            return
            
        if len(machine_code) != 12:
            messagebox.showwarning("警告", "机器码必须为12位！")
            return
            
        # 计算授权码
        auth_code = self.calculate_auth_code(machine_code)
        
        # 显示授权码
        self.auth_code_entry.config(state='normal')  # 临时设置为可编辑
        self.auth_code_entry.delete(0, tk.END)
        self.auth_code_entry.insert(0, auth_code)
        self.auth_code_entry.config(state='readonly')  # 恢复只读状态
        
        # 提示成功
        messagebox.showinfo("成功", "授权码生成成功！")
        
    def copy_auth_code(self):
        """复制授权码到剪贴板"""
        auth_code = self.auth_code_entry.get()
        
        if not auth_code:
            messagebox.showwarning("警告", "没有可复制的授权码！")
            return
            
        # 复制到剪贴板
        self.root.clipboard_clear()
        self.root.clipboard_append(auth_code)
        self.root.update()
        
        # 提示成功
        messagebox.showinfo("成功", "授权码已复制到剪贴板！")
        
    def clear_fields(self):
        """清空所有输入和输出框"""
        self.machine_code_entry.delete(0, tk.END)
        self.auth_code_entry.config(state='normal')
        self.auth_code_entry.delete(0, tk.END)
        self.auth_code_entry.config(state='readonly')


def main():
    """主函数：创建并运行应用程序"""
    # 创建主窗口
    root = tk.Tk()
    
    # 创建应用程序实例
    app = AuthorizationApp(root)
    
    # 运行主循环
    root.mainloop()


if __name__ == "__main__":
    main()
