import pandas as pd

def excel_to_json(input_file, output_file):
    try:
        # 读取 Excel 文件
        df = pd.read_excel(input_file)

        # 将 DataFrame 转换为 JSON
        json_data = df.to_json(orient='records', lines=True, force_ascii=False)

        # 将 JSON 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(json_data)

        print(f"Excel 转换为 JSON 成功，已保存至 '{output_file}'")
    except Exception as e:
        print(f"发生错误：{str(e)}")

if __name__ == "__main__":
    input_file = "input.xlsx"  # 输入的 Excel 文件名
    output_file = "output.json"  # 输出的 JSON 文件名

    excel_to_json(input_file, output_file)
