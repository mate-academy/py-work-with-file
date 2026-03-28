def create_report(data_file_name: str, report_file_name: str) -> None:
    output = {
        "supply": 0,
        "buy": 0
    }
    with open(f"{data_file_name}", "r") as file:
        for line in file.readlines():
            splited_line = line.split(",")
            output[splited_line[0]] += int(splited_line[1])
    with open(report_file_name, "w") as file:
        file.write(f"supply,{output['supply']}\n")
        file.write(f"buy,{output['buy']}\n")
        file.write(f"result,{output['supply'] - output['buy']}\n")
