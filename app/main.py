def create_report(data_file_name: str, report_file_name: str) -> None:
    old_file = open(data_file_name)
    full_text = (old_file.read()).split()
    supply = 0
    buy = 0
    for element in full_text:
        if "supply" in element:
            element = element.split(",")
            supply += int(element[1])

        if "buy" in element:
            element = element.split(",")
            buy += int(element[1])
    result = supply - buy

    old_file.close()

    with open(report_file_name, "a") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{result}\n")
