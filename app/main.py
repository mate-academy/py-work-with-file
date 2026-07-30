def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    try:
        with open(data_file_name, "r") as data:
            for line in data:
                text = line.strip()
                if text.startswith("buy"):
                    buy += int(text[4:])
                elif text.startswith("supply"):
                    supply += int(text.strip()[7:])
                else:
                    continue
    except FileNotFoundError:
        print("File hasn't been found")

    result = supply - buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{result}\n")
