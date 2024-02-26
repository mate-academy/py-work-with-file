def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if not line:
                break

            value = int(line.split(",")[1])
            if line.startswith("supply"):
                supply += value
            if line.startswith("buy"):
                buy += value

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply - buy}\n")
