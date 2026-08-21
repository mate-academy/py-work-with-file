def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {}
    with open(data_file_name) as supply_file:
        for line in supply_file:
            if not line.strip():
                continue
            splitted_line = line.split(",")
            result[splitted_line[0]] = (
                result.get(splitted_line[0], 0) + int(splitted_line[1])
            )
    with open(report_file_name, "w") as new_file:
        new_file.write(f'supply,{result["supply"]}\n')
        new_file.write(f'buy,{result["buy"]}\n')
        new_file.write(f'result,{result["supply"] - result["buy"]}\n')
