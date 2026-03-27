def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {}
    with open(data_file_name, "r") as file:
        text = file.read()
    text = text.strip().split("\n")
    for item in text:
        item = item.split(",")
        if result_dict.get(item[0]):
            result_dict[item[0]] += int(item[1])
        else:
            result_dict[item[0]] = int(item[1])
    result_dict["result"] = result_dict["supply"] - result_dict["buy"]
    new_csv = (f"supply,{result_dict['supply']}\n"
               f"buy,{result_dict['buy']}\n"
               f"result,{result_dict['result']}\n")
    with open(report_file_name, "w") as file:
        file.write(new_csv)
