def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name) as file:
        lines = file.readlines()

    for line in lines:
        if line.strip():
            operation, amount = line.split(",")
            amount = int(amount)

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    result = supply - buy

    with open(report_file_name, "a") as file:
        file.write("supply" ","f"{supply}\n")
        file.write("buy" ","f"{buy}\n")
        file.write("result" ","f"{result}\n")
