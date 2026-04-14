def create_report(data_file_name: str, report_file_name: str) -> None:

    summary = dict()
    _file = open(data_file_name, "r")
    content = _file.read().split()

    for operation in content:
        op_name = operation.split(",")[0]
        op_value = operation.split(",")[1]

        if op_name in summary:
            summary[op_name] += int(op_value)
        else:
            summary[op_name] = int(op_value)

    _file.close()

    _file = open(report_file_name, "w")

    _file.write("supply," + str(summary["supply"]) + "\n")
    _file.write("buy," + str(summary["buy"]) + "\n")

    result = summary["supply"] - summary["buy"]
    _file.write("result," + str(result) + "\n")

    _file.close()
