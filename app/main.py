def create_report(data_file_name: str, report_file_name: str) -> None:
    file_info = {}
    with open(data_file_name, "r") as file:
        for line in file.readlines():
            if len(line) != 0:
                line = line.replace("\n", "").split(",")
                key, value = line[0], line[1]
                if key not in file_info:
                    file_info[key] = value
                else:
                    file_info[key] = int(file_info[key]) + int(value)
    file_info["result"] = int(file_info["supply"]) - int(file_info["buy"])

    with open(report_file_name, "a") as file:
        file.write(f"supply,{file_info['supply']}\n")
        file.write(f"buy,{file_info['buy']}\n")
        file.write(f"result,{file_info['result']}\n")
