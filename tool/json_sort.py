import json


def sort_json_by_key(input_file, output_file):
    try:
        # 读取 JSON 文件
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 对数据按照 key 首字母进行排序
        sorted_data = sorted(data.items(), key=lambda x: x[0])

        # 将排序后的数据写入输出文件
        sorted_json = {key: value for key, value in sorted_data}
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(sorted_json, f, indent=2, ensure_ascii=False)

        print(f"JSON 文件按照 key 首字母排序成功，已保存至 '{output_file}'")
    except Exception as e:
        print(f"发生错误：{str(e)}")


if __name__ == "__main__":
    input_file = "input.json"  # 输入的 JSON 文件名
    output_file = "output_sorted.json"  # 输出的排序后的 JSON 文件名

    sort_json_by_key(input_file, output_file)
