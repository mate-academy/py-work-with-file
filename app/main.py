def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data,
          open(report_file_name, "w") as report):
        supply = 0
        buy = 0

        for line in data.readlines():
            if line != "":
                action, value = line.split(",")
                if action == "supply":
                    supply += int(value)
                elif action == "buy":
                    buy += int(value)
        result = supply - buy
        report.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{result}\n"
        )
