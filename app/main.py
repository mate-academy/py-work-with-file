def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file_to_read:
        for line in file_to_read:
            name, amount = line.split(",")
            if name == "supply":
                supply += int(amount)
            if name == "buy":
                buy += int(amount)

    with open(report_file_name, "w") as file_to_report:
        file_to_report.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
