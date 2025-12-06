using System;
using System.Windows.Forms;

namespace LicenseGenerator
{
    /// <summary>
    /// 程序入口点
    /// Application entry point
    /// </summary>
    static class Program
    {
        /// <summary>
        /// 应用程序的主入口点
        /// The main entry point for the application
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}
