def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supplied = 0
    bought = 0

    with open(data_file_name, "r") as file:
        for line in file.readlines():
            data = line.split(",")

            if data[0] == "supply":
                supplied += int(data[1])
            if data[0] == "buy":
                bought += int(data[1])

    with open(report_file_name, "a") as report:
        report.write(f"supply,{supplied}\n")
        report.write(f"buy,{bought}\n")
        report.write(f"result,{supplied - bought}\n")
