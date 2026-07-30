def create_report(
        data_file_name: str,
        report_file_name: str,
) -> None:
    supply = buy = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            key, value = line.strip().split(",")
            if key == "buy":
                buy += int(value)
            elif key == "supply":
                supply += int(value)

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{supply - buy}\n")
