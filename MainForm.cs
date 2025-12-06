using System;
using System.Drawing;
using System.Windows.Forms;

namespace LicenseGenerator
{
    /// <summary>
    /// 主窗体 - 授权码生成器
    /// Main Form - License Code Generator
    /// </summary>
    public partial class MainForm : Form
    {
        // UI 组件 / UI Components
        private Label lblTitle = null!;           // 标题标签 / Title label
        private Label lblTime = null!;            // 时间显示标签 / Time display label
        private Label lblMachineCode = null!;     // 机器码标签 / Machine code label
        private TextBox txtMachineCode = null!;   // 机器码输入框 / Machine code input box
        private Label lblAuthCode = null!;        // 授权码标签 / Authorization code label
        private TextBox txtAuthCode = null!;      // 授权码输出框 / Authorization code output box
        private Button btnGenerate = null!;       // 生成按钮 / Generate button
        private Button btnCopy = null!;           // 复制按钮 / Copy button
        private System.Windows.Forms.Timer timeTimer = null!;          // 时间更新定时器 / Time update timer

        /// <summary>
        /// 构造函数 - 初始化窗体
        /// Constructor - Initialize form
        /// </summary>
        public MainForm()
        {
            InitializeComponents();
            InitializeTimer();
        }

        /// <summary>
        /// 初始化所有UI组件
        /// Initialize all UI components
        /// </summary>
        private void InitializeComponents()
        {
            // 窗体设置 / Form settings
            this.Text = "李向前FIRE - 授权码生成器";
            this.Size = new Size(500, 400);
            this.FormBorderStyle = FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.StartPosition = FormStartPosition.CenterScreen;

            // 标题标签 / Title label
            lblTitle = new Label
            {
                Text = "李向前FIRE",
                Font = new Font("微软雅黑", 18, FontStyle.Bold),
                Location = new Point(150, 20),
                Size = new Size(200, 40),
                TextAlign = ContentAlignment.MiddleCenter
            };

            // 时间显示标签 / Time display label
            lblTime = new Label
            {
                Text = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"),
                Font = new Font("微软雅黑", 10),
                Location = new Point(140, 65),
                Size = new Size(220, 25),
                TextAlign = ContentAlignment.MiddleCenter,
                ForeColor = Color.DarkBlue
            };

            // 机器码标签 / Machine code label
            lblMachineCode = new Label
            {
                Text = "机器码 (12位):",
                Font = new Font("微软雅黑", 10),
                Location = new Point(30, 120),
                Size = new Size(120, 25)
            };

            // 机器码输入框 / Machine code input box
            txtMachineCode = new TextBox
            {
                Font = new Font("Consolas", 12),
                Location = new Point(30, 150),
                Size = new Size(420, 30),
                MaxLength = 12,  // 限制12位 / Limit to 12 characters
                CharacterCasing = CharacterCasing.Upper  // 自动转换为大写 / Auto convert to uppercase
            };
            // 添加文本改变事件 / Add text changed event
            txtMachineCode.TextChanged += TxtMachineCode_TextChanged;

            // 授权码标签 / Authorization code label
            lblAuthCode = new Label
            {
                Text = "授权码:",
                Font = new Font("微软雅黑", 10),
                Location = new Point(30, 200),
                Size = new Size(120, 25)
            };

            // 授权码输出框 / Authorization code output box
            txtAuthCode = new TextBox
            {
                Font = new Font("Consolas", 12),
                Location = new Point(30, 230),
                Size = new Size(420, 30),
                ReadOnly = true,  // 只读 / Read-only
                BackColor = Color.LightGray
            };

            // 生成按钮 / Generate button
            btnGenerate = new Button
            {
                Text = "生成授权码",
                Font = new Font("微软雅黑", 10),
                Location = new Point(30, 280),
                Size = new Size(200, 40)
            };
            btnGenerate.Click += BtnGenerate_Click;

            // 复制按钮 / Copy button
            btnCopy = new Button
            {
                Text = "复制授权码",
                Font = new Font("微软雅黑", 10),
                Location = new Point(250, 280),
                Size = new Size(200, 40)
            };
            btnCopy.Click += BtnCopy_Click;

            // 添加所有控件到窗体 / Add all controls to form
            this.Controls.Add(lblTitle);
            this.Controls.Add(lblTime);
            this.Controls.Add(lblMachineCode);
            this.Controls.Add(txtMachineCode);
            this.Controls.Add(lblAuthCode);
            this.Controls.Add(txtAuthCode);
            this.Controls.Add(btnGenerate);
            this.Controls.Add(btnCopy);
        }

        /// <summary>
        /// 初始化定时器用于更新时间显示
        /// Initialize timer for updating time display
        /// </summary>
        private void InitializeTimer()
        {
            timeTimer = new System.Windows.Forms.Timer();
            timeTimer.Interval = 1000;  // 每秒更新一次 / Update every second
            timeTimer.Tick += TimeTimer_Tick;
            timeTimer.Start();
        }

        /// <summary>
        /// 定时器触发事件 - 更新时间显示
        /// Timer tick event - Update time display
        /// </summary>
        private void TimeTimer_Tick(object? sender, EventArgs e)
        {
            lblTime.Text = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
        }

        /// <summary>
        /// 机器码输入框文本改变事件 - 确保输入符合要求
        /// Machine code textbox text changed event - Ensure input meets requirements
        /// </summary>
        private void TxtMachineCode_TextChanged(object? sender, EventArgs e)
        {
            // 输入框已经设置了自动转大写和12位限制
            // Textbox already has auto uppercase and 12 character limit set
            // 这里可以添加额外的验证逻辑
            // Additional validation logic can be added here
        }

        /// <summary>
        /// 生成授权码按钮点击事件
        /// Generate authorization code button click event
        /// </summary>
        private void BtnGenerate_Click(object? sender, EventArgs e)
        {
            // 检查机器码是否输入 / Check if machine code is entered
            if (string.IsNullOrWhiteSpace(txtMachineCode.Text))
            {
                MessageBox.Show("请输入机器码！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            // 检查机器码长度是否为12位 / Check if machine code length is 12
            if (txtMachineCode.Text.Length != 12)
            {
                MessageBox.Show("机器码必须为12位！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            // 获取机器码 / Get machine code
            string machineCode = txtMachineCode.Text.ToUpper();

            // 计算授权码 / Calculate authorization code
            string authorizationCode = CalculateAuthorizationCode(machineCode);

            // 显示授权码 / Display authorization code
            txtAuthCode.Text = authorizationCode;
        }

        /// <summary>
        /// 计算授权码的方法 - 待实现具体算法
        /// Calculate authorization code method - Algorithm to be implemented
        /// </summary>
        /// <param name="machineCode">机器码 / Machine code</param>
        /// <returns>授权码 / Authorization code</returns>
        private string CalculateAuthorizationCode(string machineCode)
        {
            // TODO: 在这里实现具体的授权码计算逻辑
            // TODO: Implement specific authorization code calculation logic here
            
            // 目前返回一个占位符，等待后续添加实际计算规律
            // Currently returns a placeholder, waiting for actual calculation pattern to be added
            
            // 临时实现：简单的示例计算（这将被实际算法替换）
            // Temporary implementation: simple example calculation (this will be replaced with actual algorithm)
            return "TEMP-" + machineCode.Substring(0, 8);
        }

        /// <summary>
        /// 复制授权码按钮点击事件
        /// Copy authorization code button click event
        /// </summary>
        private void BtnCopy_Click(object? sender, EventArgs e)
        {
            // 检查授权码是否已生成 / Check if authorization code has been generated
            if (string.IsNullOrWhiteSpace(txtAuthCode.Text))
            {
                MessageBox.Show("请先生成授权码！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            // 复制到剪贴板 / Copy to clipboard
            try
            {
                Clipboard.SetText(txtAuthCode.Text);
                MessageBox.Show("授权码已复制到剪贴板！", "成功", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch (Exception ex)
            {
                MessageBox.Show($"复制失败: {ex.Message}", "错误", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        /// <summary>
        /// 窗体关闭时清理资源
        /// Clean up resources when form closes
        /// </summary>
        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                timeTimer?.Stop();
                timeTimer?.Dispose();
            }
            base.Dispose(disposing);
        }
    }
}
