def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as input_file:
        for line in input_file.readlines():
            operation, value = line.split(",")
            if operation == "buy":
                buy += int(value)
            if operation == "supply":
                supply += int(value)
        result = supply - buy
    with open(report_file_name, "w") as output_file:
        output_file.write(f"supply,{supply}\n")
        output_file.write(f"buy,{buy}\n")
        output_file.write(f"result,{result}\n")
