def create_report(data_file_name: str, report_file_name: str) -> None:
    goods = {
        "supply": 0,
        "buy": 0
    }
    with open(data_file_name, "r") as input_data:
        while True:
            line_content = input_data.readline()
            if line_content == "":
                break
            operation, amount = line_content.replace("\n", "").split(",")
            goods[operation] += int(amount)
    with open(report_file_name, "w") as report:
        report.write(f"supply,{goods['supply']}\n"
                     f"buy,{goods['buy']}\n"
                     f"result,{goods['supply'] - goods['buy']}\n")
