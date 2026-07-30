def create_report(data_file_name: str, report_file_name: str) -> None:
    temp = {
        "supply": [],
        "buy": [],
    }

    input_file = open(data_file_name, "tr")
    for index in input_file.readlines():
        key, value = index.split(",")
        temp[key].append(int(value))
    input_file.close()

    output_file = open(report_file_name, "tw")
    for key, value_list in temp.items():
        temp[key] = sum(temp[key])
        output_file.write(f"{key},{temp[key]}\n")
    output_file.write(f"result,{temp['supply'] - temp['buy']}\n")
    output_file.close()
