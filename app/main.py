def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    operations = {"supply": 0, "buy": 0}

    with open(data_file_name, "r", newline="") as data:
        for line in data.readlines():
            operation_type, amount = line.split(",")
            operations[operation_type] += int(amount)
    str_supply = str(operations["supply"])
    str_buy = str(operations["buy"])
    str_res = str(operations["supply"] - operations["buy"])
    lines = [f"supply,{str_supply}\n",
             f"buy,{str_buy}\n",
             f"result,{str_res}\n"]
    with open(report_file_name, "w") as report:
        report.writelines(lines)
