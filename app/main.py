def create_report(data_file_name: str, report_file_name: str) -> None:
    if data_file_name and report_file_name:
        try:
            with open(data_file_name, "r") as data:
                with open(report_file_name, "w") as report:
                    buy, supply = 0, 0
                    for line in data:
                        op, amount = line.split(",")
                        if op == "buy":
                            buy += int(amount)
                        if op == "supply":
                            supply += int(amount)
                    report.write(f"supply,{supply}\n")
                    report.write(f"buy,{buy}\n")
                    report.write(f"result,{supply - buy}\n")

        except (FileNotFoundError):
            pass
