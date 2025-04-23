def create_report(data_file_name: str, report_file_name: str) -> None:
    new_data = {}
    data_file = open(data_file_name, "r")
    for line in data_file:
        line = line.strip()
        key, value = line.split(",", 1)
        if key in new_data:
            new_data[key] += int(value)
        else:
            new_data[key] = int(value)
    data_file.close()
    new_data.update({"result": new_data["supply"] - new_data["buy"]})
    report_file = open(report_file_name, "w")
    report_file.write(f'supply,{new_data["supply"]}\n')
    report_file.write(f'buy,{new_data["buy"]}\n')
    report_file.write(f'result,{new_data["result"]}\n')
    report_file.close()
