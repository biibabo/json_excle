from tool.json_compare import compare_json_files

if __name__ == "__main__":
    file1 = "./../data/json/库-利润表_sorted.json"  # 第一个 JSON 文件名
    file2 = "./../data/json/接口-利润表_sorted.json"  # 第二个 JSON 文件名
    #
    result = compare_json_files(file1, file2)
    print("JSON 文件比对结果：", result)
