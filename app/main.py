def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    operation_dict = {}
    for line in data_file.readlines():
        name, price = line.split(",")
        if name not in operation_dict:
            operation_dict[name] = int(price)
        operation_dict[name] += int(price)
    data_file.close()

    report_file = open(report_file_name, "w")
    for key, value in operation_dict.items():
        report_file.write(f"{key},{value}\n")
    report_file.close()
