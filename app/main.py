def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {
        "supply": 0,
        "buy": 0,
    }
    with open(data_file_name, "r") as f:
        for line in f.readlines():
            line = line.split(",")
            if line[0] in data_dict:
                data_dict[line[0]] += int(line[1])

    with open(report_file_name, "w") as f:
        f.write(f"supply,{data_dict['supply']}\n")
        f.write(f"buy,{data_dict['buy']}\n")
        f.write(f"result,{data_dict['supply'] - data_dict['buy']}\n")
