def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data,\
            open(report_file_name, "w") as report:
        for line in data.read().split():
            if line.split(",")[0] == "supply":
                supply += int(line.split(",")[1])
            if line.split(",")[0] == "buy":
                buy += int(line.split(",")[1])

        result = supply - buy

        report.write(f"supply,{supply}\n"
                     f"buy,{buy}\n"
                     f"result,{result}\n")
