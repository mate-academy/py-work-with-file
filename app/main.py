def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {"supply": 0, "buy": 0}

    with open(data_file_name) as data_file:
        for line in data_file:
            current_line = tuple(line.replace("\n", "").split(","))
            result[current_line[0]] += int(current_line[1])

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{result['supply']}\n"
                          f"buy,{result['buy']}\n"
                          f"result,{result['supply'] - result['buy']}\n")
