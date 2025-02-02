import requests
import importlib.util
import os

url = os.getenv("URL")
response = requests.get(url)

if response.status_code == 200:
    with open("remote_module.py", "w", encoding="utf-8") as f:
        f.write(response.text)

    spec = importlib.util.spec_from_file_location("remote_module", "remote_module.py")
    remote_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(remote_module)

    # 调用远程模块的函数
    if hasattr(remote_module, "main"):
        remote_module.main()
