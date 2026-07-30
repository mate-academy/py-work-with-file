def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    result = 0
    with open(data_file_name, "r") as data:
        for line in data:
            key, value = line.split(",")
            if key == "supply":
                supply += int(value)
            if key == "buy":
                buy += int(value)
        result = supply - buy

    with open(report_file_name, "w") as report:
        report.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{result}\n"
        )


# create_report("data.csv", "report.csv")
