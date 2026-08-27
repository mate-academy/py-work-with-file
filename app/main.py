def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        data = file.read()
        data = data.split("\n")
    for row in data:
        if row != "":
            operation_type, amount = row.split(",")
            amount = int(amount)
            if operation_type == "buy":
                buy += amount
            if operation_type == "supply":
                supply += amount
    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write("supply," + str(supply) + "\n")
        report_file.write("buy," + str(buy) + "\n")
        report_file.write("result," + str(result) + "\n")
