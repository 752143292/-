# 开发者指南 - 添加授权码计算算法

本文档说明如何将实际的授权码计算规律添加到程序中。

## 位置

需要修改的函数位于 `authorization_app.py` 文件中的 `calculate_auth_code()` 方法。

**文件：** `authorization_app.py`  
**函数位置：** 约第207-234行  
**类：** `AuthorizationApp`

## 当前占位代码

```python
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
    
    # 验证机器码格式（仅包含字母数字）
    if not machine_code.isalnum():
        return "ERROR-INVALID-FORMAT"
        
    # 临时示例：简单处理（实际使用时需替换）
    # 这里只是一个占位符，展示返回格式
    # 实际算法应根据具体的计算规律实现
    example_auth_code = f"AUTH-{machine_code}-DEMO"
    
    return example_auth_code
```

## 修改步骤

### 步骤1：了解计算规律

首先，您需要明确授权码的计算规律。例如：

**示例规律：**
- 将机器码的每个字符转换为ASCII码
- 对ASCII码进行某种数学运算
- 将结果转换为特定格式的授权码
- 等等...

### 步骤2：实现计算逻辑

根据您的计算规律，替换占位代码。以下是几个示例：

#### 示例1：简单的字符反转 + 校验和

```python
def calculate_auth_code(self, machine_code):
    """
    计算授权码的函数
    规律：反转机器码 + 添加校验和
    """
    if not machine_code:
        return ""
    
    # 验证格式
    if not machine_code.isalnum():
        return "ERROR-INVALID-FORMAT"
    
    # 反转字符串
    reversed_code = machine_code[::-1]
    
    # 计算校验和（所有字符ASCII值之和的后4位）
    checksum = sum(ord(c) for c in machine_code) % 10000
    
    # 组合授权码
    auth_code = f"{reversed_code}-{checksum:04d}"
    
    return auth_code
```

#### 示例2：基于位置的数学运算

```python
def calculate_auth_code(self, machine_code):
    """
    计算授权码的函数
    规律：每个字符的ASCII码 * 位置索引
    """
    if not machine_code:
        return ""
    
    if not machine_code.isalnum():
        return "ERROR-INVALID-FORMAT"
    
    # 计算每个字符的值
    values = []
    for i, char in enumerate(machine_code, 1):
        value = ord(char) * i
        values.append(str(value % 100))  # 取后两位
    
    # 组合授权码
    auth_code = "-".join(values)
    
    return auth_code
```

#### 示例3：使用哈希算法

```python
import hashlib

def calculate_auth_code(self, machine_code):
    """
    计算授权码的函数
    规律：使用MD5哈希并截取部分字符
    """
    if not machine_code:
        return ""
    
    if not machine_code.isalnum():
        return "ERROR-INVALID-FORMAT"
    
    # 计算MD5哈希
    hash_obj = hashlib.md5(machine_code.encode())
    hash_hex = hash_obj.hexdigest()
    
    # 截取并格式化
    auth_code = f"{hash_hex[:8].upper()}-{hash_hex[8:16].upper()}"
    
    return auth_code
```

**注意：** 如果使用示例3，需要在文件顶部添加导入：
```python
import hashlib
```

#### 示例4：自定义查找表

```python
def calculate_auth_code(self, machine_code):
    """
    计算授权码的函数
    规律：使用自定义字符映射表
    """
    if not machine_code:
        return ""
    
    if not machine_code.isalnum():
        return "ERROR-INVALID-FORMAT"
    
    # 自定义映射表
    char_map = {
        'A': '9', 'B': '8', 'C': '7', 'D': '6', 'E': '5',
        'F': '4', 'G': '3', 'H': '2', 'I': '1', 'J': '0',
        'K': 'Z', 'L': 'Y', 'M': 'X', 'N': 'W', 'O': 'V',
        'P': 'U', 'Q': 'T', 'R': 'S', 'S': 'R', 'T': 'Q',
        'U': 'P', 'V': 'O', 'W': 'N', 'X': 'M', 'Y': 'L',
        'Z': 'K', '0': 'J', '1': 'I', '2': 'H', '3': 'G',
        '4': 'F', '5': 'E', '6': 'D', '7': 'C', '8': 'B',
        '9': 'A'
    }
    
    # 转换每个字符
    auth_code = ''.join(char_map.get(c, c) for c in machine_code)
    
    # 添加分隔符
    auth_code = f"{auth_code[:4]}-{auth_code[4:8]}-{auth_code[8:]}"
    
    return auth_code
```

### 步骤3：测试您的算法

修改代码后，建议先运行测试：

```bash
# 运行语法检查
python -m py_compile authorization_app.py

# 运行程序测试
python authorization_app.py
```

在程序中测试几个机器码，确保：
1. 计算结果正确
2. 没有错误发生
3. 授权码格式符合预期

### 步骤4：更新测试用例（可选）

如果您想添加自动化测试，可以修改 `test_authorization.py` 文件：

```python
def test_auth_code_generation():
    """测试授权码生成"""
    print("测试3: 授权码生成")
    
    class TempApp:
        def calculate_auth_code(self, machine_code):
            # 复制您的实际计算逻辑
            if not machine_code:
                return ""
            # ... 您的算法 ...
            return calculated_result
    
    app = TempApp()
    
    # 添加实际的测试用例
    test_cases = [
        ("ABC123DEF456", "期望的授权码1"),
        ("123456789012", "期望的授权码2"),
        ("", ""),
    ]
    
    for input_code, expected in test_cases:
        result = app.calculate_auth_code(input_code)
        assert result == expected, f"失败: {input_code} -> {result}, 期望 {expected}"
        print(f"  ✓ {input_code} -> {result}")
    
    print("  测试通过！\n")
```

### 步骤5：重新构建exe（如果需要）

修改完成并测试通过后，重新构建exe文件：

**Windows:**
```bash
build.bat
```

**Linux/Mac:**
```bash
./build.sh
```

## 常见问题

### Q1: 我需要使用第三方库怎么办？

如果您的算法需要第三方库（如 `pycryptodome`, `numpy` 等）：

1. 在 `requirements.txt` 中添加依赖：
   ```
   pyinstaller>=5.0
   pycryptodome>=3.15.0  # 您的新依赖
   ```

2. 在代码顶部导入：
   ```python
   from Crypto.Cipher import AES  # 示例
   ```

3. 重新构建时会自动包含这些库

### Q2: 如何处理错误的机器码？

在 `calculate_auth_code()` 函数中添加验证：

```python
def calculate_auth_code(self, machine_code):
    # 检查是否为空
    if not machine_code:
        return ""
    
    # 检查长度
    if len(machine_code) != 12:
        return "ERROR-LENGTH"
    
    # 检查格式（只允许字母数字）
    if not machine_code.isalnum():
        return "ERROR-FORMAT"
    
    # 其他自定义验证
    if not machine_code.startswith('ABC'):
        return "ERROR-PREFIX"
    
    # 通过验证后进行计算
    # ... 您的计算逻辑 ...
```

### Q3: 授权码需要更长或更短怎么办？

授权码的长度没有限制，您可以返回任意长度的字符串。界面会自动调整显示。

### Q4: 可以让授权码包含特殊字符吗？

可以！授权码可以包含任何字符（包括中文、特殊符号等），例如：
```python
auth_code = f"授权-{machine_code}-验证码"
```

### Q5: 如何加密算法防止被破解？

1. **使用编译后的.exe**：PyInstaller打包的exe会将代码编译，难以直接查看
2. **添加混淆**：使用 `pyarmor` 等工具对代码进行混淆
3. **服务器端验证**：将关键算法放在服务器端，程序只负责通信

## 调试技巧

### 添加调试输出

在开发过程中，可以添加打印语句：

```python
def calculate_auth_code(self, machine_code):
    print(f"[DEBUG] 输入机器码: {machine_code}")
    
    # 您的计算逻辑
    result = "..."
    
    print(f"[DEBUG] 计算结果: {result}")
    return result
```

### 使用日志文件

如果需要保存日志：

```python
import logging

# 在类初始化时配置日志
logging.basicConfig(
    filename='auth_generator.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def calculate_auth_code(self, machine_code):
    logging.info(f"计算授权码，机器码: {machine_code}")
    
    # 计算逻辑
    result = "..."
    
    logging.info(f"生成授权码: {result}")
    return result
```

## 提供算法规律时的格式

当您准备好提供计算规律时，请提供以下信息：

1. **算法描述**：用文字描述计算过程
2. **示例数据**：提供3-5组机器码和对应的授权码
3. **特殊规则**：是否有特殊字符处理、验证规则等

**示例格式：**

```
算法描述：
1. 将机器码每3个字符分为一组
2. 每组字符的ASCII值相加
3. 结果转换为16进制
4. 用-连接各组

示例数据：
机器码：ABC123DEF456
授权码：计算结果示例

机器码：XYZ789GHI012
授权码：计算结果示例

特殊规则：
- 如果机器码包含'000'，授权码前缀加'SPEC-'
- 授权码全部转换为大写
```

有了这些信息，就可以准确实现您的计算规律了！

---

**需要帮助？**  
如果在实现算法时遇到问题，请提供：
- 错误信息
- 测试的机器码
- 期望的授权码
- 实际得到的授权码
