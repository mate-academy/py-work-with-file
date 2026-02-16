def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    data_file = open(data_file_name, "r")

    buy = 0
    supply = 0

    for data_line in data_file:
        if data_line == "":
            break
        service, value = data_line.split(",")
        value = int(value)

        if service == "buy":
            buy += value
        else:
            supply += value

    data_file.close()
    result = supply - buy

    report_file = open(report_file_name, "w")

    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{result}\n")

    report_file.close()
