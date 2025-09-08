def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line_parts = line.strip().split(",")
            if line_parts[0] == "supply":
                supply += int(line_parts[1])
            elif line_parts[0] == "buy":
                buy += int(line_parts[1])

    result = supply - buy
    report = f"supply,{supply}\nbuy,{buy}\nresult,{result}\n"

    with open(report_file_name, "w") as file:
        file.write(report)
