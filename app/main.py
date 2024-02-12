def create_report(data_file_name: str, report_file_name: str) -> None:

    supply = 0
    buy = 0

    with open(data_file_name, "r") as data_file:
        for data in data_file:
            content = data.split(",")
            if content[0] == "supply":
                supply += int(content[1])
            if content[0] == "buy":
                buy += int(content[1])

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\nbuy,{buy}\n"
                          f"result,{supply - buy}\n")
