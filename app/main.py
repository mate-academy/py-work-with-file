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

    supply = report_dict["supply"]
    buy = report_dict["buy"]

    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{supply - buy}\n")

    report_file.close()
