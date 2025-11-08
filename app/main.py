def create_report(data_file_name: str, report_file_name: str) -> None:
    new_data = {}
    with open(data_file_name, "r") as file:
        for data in file:
            key, value = data.strip().split(",")
            new_data[key] = new_data.get(key, 0) + int(value)
        new_data["result"] = new_data["supply"] - new_data["buy"]

    with open(report_file_name, "w") as new_file:
        new_file.write(f'supply,{new_data["supply"]}\n'
                       f'buy,{new_data["buy"]}\n'
                       f'result,{new_data["result"]}\n'
                       )
