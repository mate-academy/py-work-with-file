def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, 'r') as opened_file:
        result = {"supply": 0, "buy": 0}
        for row in opened_file.readlines():
            result[row.split(",")[0]] += int(row.split(",")[1])

    with open(report_file_name, "w") as opened_file:
        opened_file.write(f"supply,{result['supply']}\n"
                          f"buy,{result['buy']}\n"
                          f"result,{result['supply'] - result['buy']}\n")
