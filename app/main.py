def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            parts = line.split(",")

            if parts[0] == "supply":
                supply += int(parts[1])
            if parts[0] == "buy":
                buy += int(parts[1])

    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
