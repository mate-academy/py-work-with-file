def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        content = file.read().split("\n")
        for line in content:
            operation = line.split(",")
            if operation[0] == "supply":
                supply += int(operation[1])
            elif operation[0] == "buy":
                buy += int(operation[1])

    with open(report_file_name, "w") as result_file:
        result_file.write(f"supply,{supply}\n")
        result_file.write(f"buy,{buy}\n")
        result_file.write(f"result,{supply - buy}\n")
