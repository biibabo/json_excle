
from tool.excle_to_json import excel_to_json

if __name__ == "__main__":
    input_file = "../data/excle/test.xlsx"  # 输入的 Excel 文件名
    output_file = "./../data//json/test.json"  # 输出的 JSON 文件名

    excel_to_json(input_file, output_file)
