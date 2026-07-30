def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {
        "supply": 0,
        "buy": 0,
    }

    with open(data_file_name, "r") as file:
        for line in file:
            if line:
                value = line.split(",")
                result[value[0]] += int(value[1])

    with open(report_file_name, "w") as file:
        file.write(f"supply,{result['supply']}\n")
        file.write(f"buy,{result['buy']}\n")
        file.write(f"result,{result['supply'] - result['buy']}\n")
