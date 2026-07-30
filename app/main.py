def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data_file:
        supply = 0
        buy = 0

        for line in data_file:
            action, amount = line.split(",")
            if action.lower() == "supply":
                supply += int(amount)
            elif action.lower() == "buy":
                buy += int(amount)
            else:
                raise ValueError(f"Invalid value {action}")

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply - buy}\n")
