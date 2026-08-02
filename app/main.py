def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        lines = data_file.read().splitlines()

    new_lines = []
    for line in lines:
        line_list = line.split(",")
        new_lines.append(line_list)

    supply = 0
    buy = 0
    for item in new_lines:
        if item[0] == "supply":
            supply += int(item[1])
        elif item[0] == "buy":
            buy += int(item[1])

    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
