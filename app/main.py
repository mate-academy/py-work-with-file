def create_report(data_file_name: str, report_file_name: str):
    operation_type = {
        "supply": 0,
        "buy": 0
    }

    with open(data_file_name, "r") as df:
        with open(report_file_name, "w") as rf:
            for line in df:
                line = line.split(",")
                operation_type[line[0]] += int(line[1])

            result = operation_type["supply"] - operation_type["buy"]

            rf.write(f"supply,{operation_type['supply']}\n")
            rf.write(f"buy,{operation_type['buy']}\n")
            rf.write(f"result,{result}\n")
