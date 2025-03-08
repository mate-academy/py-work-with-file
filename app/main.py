def create_report(data_file_name: str, report_file_name: str) -> None:
    report_file = open(report_file_name, "w")
    data_file = open(data_file_name, "r")

    report_dict = {"supply": 0, "buy": 0}

    for line in data_file.readlines():
        if line.split(",")[0] == "supply":
            report_dict["supply"] += int(line.split(",")[1])
        else:
            report_dict["buy"] += int(line.split(",")[1])
    data_file.close()

    report_file.write(f"supply,{report_dict.get("supply")}\n")
    report_file.write(f"buy,{report_dict.get("buy")}\n")
    report_file.write(f"result,"
                      f"{report_dict.get("supply") - report_dict.get("buy")}"
                      f"\n")

    report_file.close()
