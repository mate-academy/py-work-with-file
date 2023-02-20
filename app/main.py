def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supplied = 0
    bought = 0

    with open(data_file_name, "r") as input_file:
        for line in input_file.readlines():
            data = line.split(",")

            if data[0] == "supply":
                supplied += int(data[1])
            if data[0] == "buy":
                bought += int(data[1])

    with open(report_file_name, "a") as report_file:
        report_file.write(f"supply,{supplied}\n")
        report_file.write(f"buy,{bought}\n")
        report_file.write(f"result,{supplied - bought}\n")
