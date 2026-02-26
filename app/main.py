def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as f:
        for line in f.readlines():
            if not line:
                break
            sort, number = line.split(",")
            data_dict[sort] += int(number)
    result = data_dict["supply"] - data_dict["buy"]
    with open(report_file_name, "w") as f:
        f.write(f"supply,{data_dict['supply']}\n")
        f.write(f"buy,{data_dict['buy']}\n")
        f.write(f"result,{result}\n")
