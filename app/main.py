def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as file:

        buy = 0
        supply = 0

        for line in file.read().split("\n"):
            if not line:
                break
            operation, amount = line.split(",")
            if operation == "buy":
                buy += int(amount)
            if operation == "supply":
                supply += int(amount)

    result = supply - buy

    with (open(report_file_name, "w") as report):
        output = "supply,"
        output += f"{supply}\n"
        output += "buy,"
        output += f"{buy}\n"
        output += "result,"
        output += f"{result}\n"

        report.write(output)
