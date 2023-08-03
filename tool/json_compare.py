import json


def compare_json(json1, json2):
    try:
        data1 = json.loads(json1)
        data2 = json.loads(json2)

        if data1 is None or data2 is None:
            return False

        if data1 == data2:
            print("JSON 数据完全相同")
            return True
        else:
            print("JSON 数据比对失败：")
            for key, value1 in data1.items():
                value2 = data2.get(key, None)
                if value1 != value2:
                    print(f"Key: '{key}', Value1: '{value1}', Value2: '{value2}'")
            return False
    except Exception as e:
        print(f"发生错误：{str(e)}")
        return False


def compare_json_files(file1, file2):
    try:
        # 读取第一个 JSON 文件
        with open(file1, 'r', encoding='utf-8') as f1:
            json1 = f1.read()

        # 读取第二个 JSON 文件
        with open(file2, 'r', encoding='utf-8') as f2:
            json2 = f2.read()

        return compare_json(json1, json2)
    except Exception as e:
        print(f"发生错误：{str(e)}")
        return False


if __name__ == "__main__":
    file1 = "input1.json"  # 第一个 JSON 文件名
    file2 = "input2.json"  # 第二个 JSON 文件名

    result = compare_json_files(file1, file2)
    print("JSON 文件比对结果：", result)
