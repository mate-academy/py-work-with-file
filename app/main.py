def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            clean_line = line.strip()

            action, amount = clean_line.split(",")

            if action == "buy":
                buy += int(amount)
            elif action == "supply":
                supply += int(amount)

    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
