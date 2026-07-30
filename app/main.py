def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    with open(data_file_name, "r") as data_file:
        report = {}

        for line in data_file:
            key, value = line.split(",")
            try:
                if key in report:
                    report[key] += int(value)
                else:
                    report[key] = int(value)
            except ValueError:
                print(f"Cannot convert {value} into integer.")

    result_report = [
        f"supply,{report['supply']}",
        f"buy,{report['buy']}",
        f"result,{report['supply'] - report['buy']}",
    ]

    with open(report_file_name, "w") as report_file:
        report_file.write("\n".join(result_report) + "\n")
