def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            keyword, value = line.split(",")
            value = int(value)

            if keyword == "supply":
                supply += value
            elif keyword == "buy":
                buy += value

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
