def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0

    with open(data_file_name, "r") as file:
        for content in file:
            if not content:
                break

            amount = int(content.split(",")[1])
            if content.startswith("supply"):
                supply += amount
            if content.startswith("buy"):
                buy += amount

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply, {supply}\n")
        report_file.write(f"buy, {buy}\n")
        report_file.write(f"result, {supply - buy}\n")
