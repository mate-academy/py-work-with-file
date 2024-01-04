def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(data_file_name, "r") as data_file:
        supply = 0
        buy = 0
        for line in data_file.readlines():
            columns = line.strip().split(",")

            operation_type = columns[0]
            amount = int(columns[1])

            if operation_type == "supply":
                supply += amount
            elif operation_type == "buy":
                buy += amount
        result = supply - buy

    with open(report_file_name, "a") as data_file:
        data_file.write(f"supply,{supply}\n")
        data_file.write(f"buy,{buy}\n")
        data_file.write(f"result,{result}\n")
