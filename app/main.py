def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {}

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            operation, value = line.split(",")
            if operation in data:
                data[operation] += int(value)
            else:
                data[operation] = int(value)

    result = 0
    for oper in data:
        if oper == "supply":
            result += int(data[oper])
        if oper == "buy":
            result -= int(data[oper])

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{data['supply']}\n")
        report_file.write(f"buy,{data['buy']}\n")
        report_file.write(f"result,{result}\n")
