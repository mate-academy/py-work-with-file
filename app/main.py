def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name) as data_file:
        lines = data_file.readlines()
    if len(lines[-1]) == 0:
        lines.pop(-1)
    supply = 0
    buy = 0
    for line in lines:
        line = line.split(",")
        if line[0] == "supply":
            supply += int(line[1])
        if line[0] == "buy":
            buy += int(line[1])
    result = supply - buy
    with open(report_file_name, "a") as report:
        report.writelines(f"supply,{supply}\n")
        report.writelines(f"buy,{buy}\n")
        report.writelines(f"result,{result}\n")
