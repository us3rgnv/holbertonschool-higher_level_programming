# Python - Network #1  
This project contains tasks for learning how to use `urllib` in Python to handle URLs and HTTP requests.

## Task: 0-hbtn_status.py

### 🔹 Description  
Write a Python script that fetches **https://intranet.hbtn.io/status**

Requirements:
- Must use the package **urllib**
- **No other imports allowed**
- Must use a **with statement**
- Body of the response must follow this exact format:

Example output:

---

## 📌 File: `0-hbtn_status.py`

```python
#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
