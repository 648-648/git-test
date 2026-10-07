"""一个最小的测试脚本，用来确认仓库能正常保存并推送代码文件。"""


def greet(name: str) -> str:
    return f"你好，{name}！Git 推送链路正常。"


if __name__ == "__main__":
    print(greet("世界"))
    print(greet("GitHub"))
