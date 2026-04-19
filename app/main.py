def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {}

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            parts = line.strip().split(",")
            # print(parts)
            if parts != "\n":
                report_dict[parts[0]] = report_dict.get(parts[0],
                                                        0) + int(parts[1])

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{report_dict['supply']}\n")
        report_file.write(f"buy,{report_dict['buy']}\n")
        report_file.write(
            f"result,{int(report_dict['supply'] - report_dict['buy'])}\n"
        )
