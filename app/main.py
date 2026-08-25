def create_report(data_file_name: str, report_file_name: str) -> None:
    map_data = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as source_file, open(
        report_file_name, "w"
    ) as report_file:
        for line in source_file:
            if line:
                data_from_line = line.split(",")
                map_data[data_from_line[0]] += int(data_from_line[1])

        map_data["result"] = map_data["supply"] - map_data["buy"]

        report_file.write(f'supply,{map_data["supply"]}\n')
        report_file.write(f'buy,{map_data["buy"]}\n')
        report_file.write(f'result,{map_data["result"]}\n')
