# WZU Srun Login

温州大学深澜 (Srun) 校园网认证登录脚本，纯 Python 实现。

## 特性

- 纯 Python 实现完整的 Srun `srun_bx1` 加密协议 (XXTEA + 自定义 Base64 + HMAC-MD5 + SHA-1)
- 仅依赖 `requests` 库，无 Node.js / execjs 依赖
- 支持命令行参数和交互式输入两种方式
- 提供 Shell 封装脚本，适用于 cron 定时登录等自动化场景

## 依赖

- Python 3.6+
- requests

## 安装

```bash
git clone https://github.com/CHENG-danyang/Srun-login.git
cd Srun-login
pip install -r requirements.txt
```

## 使用方法

### 命令行模式

```bash
python login.py --username=学号 --passwd=密码 --login_host=网关IP
```

### 交互模式

不传参数，脚本会依次提示输入：

```bash
python login.py
```

### Shell 封装 (自动化 / cron)

编辑 `login.sh`，填入你的账号信息和虚拟环境路径后运行：

```bash
bash login.sh
```

## 参数说明

| 参数 | 说明 |
|------|------|
| `--username` | 校园网账号（学号） |
| `--passwd` | 校园网密码 |
| `--login_host` | 登录网关地址（在浏览器登录页面查看地址栏获取） |

## 项目结构

```
.
├── login.py          # 主入口，登录流程编排
├── login.sh          # Bash 封装脚本
├── args.py           # 命令行参数解析
├── encode.py         # 自定义 Base64 编码 + encodeUserInfo
├── xxtea.py          # XXTEA 加密算法
├── jQuery.py         # 模拟 jQuery callback 生成
├── md5.py            # HMAC-MD5 密码哈希
└── requirements.txt  # Python 依赖
```

## 认证流程

1. 向 `/cgi-bin/get_challenge` 请求获取 challenge token
2. 对密码和 token 进行 HMAC-MD5 哈希
3. 使用 XXTEA 加密用户信息 (用户名、密码、IP 等)，并以自定义 Base64 编码
4. 计算 SHA-1 校验和
5. 将加密后的信息提交至 `/cgi-bin/srun_portal` 完成登录

## 注意事项

- Shell 脚本中含明文密码，请注意文件权限安全
- 本项目仅适用于温州大学深澜校园网认证系统

## 致谢

原作者：D.Y.Cheng ([dycheng.tech@outlook.com](mailto:dycheng.tech@outlook.com))

GitHub: [https://github.com/CHENG-danyang/Srun-login](https://github.com/CHENG-danyang/Srun-login)
