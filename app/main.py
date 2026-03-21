def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name)

    supply = 0
    buy = 0

    for row in data_file.readlines():
        operation = row.split(",")
        if operation[0] == "supply":
            supply += int(operation[1])
        else:
            buy += int(operation[1])

    data_file.close()

    data_file = open(report_file_name, "a")

    data_file.write(f"supply,{supply}\n")
    data_file.write(f"buy,{buy}\n")
    data_file.write(f"result,{supply - buy}\n")

    data_file.close()
