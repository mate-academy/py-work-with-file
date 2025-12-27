def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as input_file:
        for line in input_file.readlines():
            operation, num = line.split(",")
            if operation == "supply":
                supply += int(num)

            if operation == "buy":
                buy += int(num)

    with open(report_file_name, "w") as output_file:
        output_file.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{supply - buy}\n"
                          f"")
