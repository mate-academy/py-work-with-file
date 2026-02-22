def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as f:
        for line in f:
            key, value = line.split(",")
            report_dict[key] += int(value)

    report_dict["result"] = report_dict["supply"] - report_dict["buy"]

    with open(report_file_name, "w") as f:
        f.write("\n".join(f"{key},{value}"
                          for key, value in report_dict.items()) + "\n")
