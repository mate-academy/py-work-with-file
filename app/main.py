def create_report(data_file_name: str, report_file_name: str) -> None:

    file_to_read = open(data_file_name, "r")
    supply = 0
    buy = 0

    file_lines = file_to_read.readlines()
    for line in file_lines :
        line = line.strip()
        if not line:
            continue
        action, amount = line.split(",")
        if action == "supply":
            supply += int(amount)
        if action == "buy":
            buy += int(amount)

    result = supply - buy

    file_to_read.close()

    report = open(report_file_name, "w")
    report.write(f"supply,{supply}\n")
    report.write(f"buy,{buy}\n")
    report.write(f"result,{result}\n")

    report.close()
