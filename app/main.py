def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    operation_dict = {}
    result = 0
    for line in data_file.readlines():
        name, price = line.split(",")
        if name not in operation_dict:
            operation_dict[name] = int(price)
        operation_dict[name] += int(price)
        if name == "buy":
            result -= int(price)
        if name == "supply":
            result += int(price)

    data_file.close()
    operation_dict["result"] = result

    report_file = open(report_file_name, "w")
    for key, value in operation_dict.items():
        report_file.write(f"{key},{value}\n")
    report_file.close()
