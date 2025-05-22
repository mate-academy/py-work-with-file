def create_report(data_file_name: str, report_file_name: str) -> None:
    source_file = f"..\\{data_file_name}"
    output_file = f"..\\tests\\{report_file_name}"
    report_dict = {"supply": 0, "buy": 0}

    with open(source_file, "r") as f:
        for line in f:
            key, value = line.split(",")
            report_dict[key] += int(value)

    report_dict["result"] = report_dict["supply"] - report_dict["buy"]

    with open(output_file, "w") as f:
        f.write("\n".join(f"{key},{value}"
                          for key, value in report_dict.items()) + "\n")
