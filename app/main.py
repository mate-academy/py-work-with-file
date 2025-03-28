def create_report(data_file_name: str, report_file_name: str) -> None:
    text = []
    result_dict = {}
    with open(data_file_name, "r") as file:
        for line in file:
            text.append(line.split(","))
    for i in text:
        if i[0] in result_dict:
            result_dict[i[0]] += int(i[1].replace("\n", ""))
        else:
            result_dict[i[0]] = int(i[1].replace("\n", ""))
    result_dict["result"] = result_dict["supply"] - result_dict["buy"]
    with open(report_file_name, "a") as new_file:
        new_file.writelines(f"supply,{result_dict['supply']}\n")
        new_file.writelines(f"buy,{result_dict['buy']}\n")
        new_file.writelines(f"result,{result_dict['result']}\n")
