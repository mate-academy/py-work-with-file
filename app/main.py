def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as file:
        for line in file:
            tmp = line.split(",")
            if tmp[0] == "supply":
                report_dict["supply"] += int(tmp[1])
            if tmp[0] == "buy":
                report_dict["buy"] += int(tmp[1])

    with open(report_file_name, mode="w") as file:
        file.write(f"supply,{report_dict['supply']}\n")
        file.write(f"buy,{report_dict['buy']}\n")
        file.write(f"result,{report_dict['supply'] - report_dict['buy']}\n")
