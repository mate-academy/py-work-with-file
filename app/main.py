def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as input_file:
        for line in input_file.readlines():
            data = line.split(",")

            if data[0] == "supply":
                supply += int(data[1])
            if data[0] == "buy":
                buy += int(data[1])

    with open(report_file_name, "a") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply - buy}\n")
