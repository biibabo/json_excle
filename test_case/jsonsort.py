from tool.json_sort import sort_json_by_key


if __name__ == "__main__":
    input_file = "./../data/json/接口-利润表.json"  # 输入的 JSON 文件名
    output_file = "./../data/json/接口-利润表_sorted.json"  # 输出的排序后的 JSON 文件名

    sort_json_by_key(input_file, output_file)

