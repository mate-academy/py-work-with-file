def create_report(data_file_name: str,
                  report_file_name: str) -> None:

    result = {}

    with open(data_file_name, "r") as source:
        for line in source:
            key, value = line.split(",")
            if key in result:
                result[key] += int(value)
            else:
                result[key] = int(value)

    with open(report_file_name, "w") as report:
        report.write(f"supply,{result['supply']}\n"
                     f"buy,{result['buy']}\n"
                     f"result,{result['supply'] - result['buy']}\n")
