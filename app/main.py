def create_report(data_file_name: str, report_file_name: str) -> None:
    read_file = open(data_file_name)
    operations = {}
    for line in read_file.readlines():
        if line:
            operation = line.split(",")
            if operation[0] in operations:
                operations[operation[0]] += int(operation[1])
            else:
                operations.update({operation[0]: int(operation[1])})
    read_file.close()
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{operations["supply"]}\n")
    report_file.write(f"buy,{operations["buy"]}\n")
    report_file.write(f"result,{operations["supply"] - operations["buy"]}\n")
    report_file.close()
