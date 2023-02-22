def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {}
    with open(data_file_name, "r") as data_file:
        for line in data_file.read().splitlines():
            temp_data = line.split(",")
            if temp_data[0] not in data_dict:
                data_dict[temp_data[0]] = 0
            data_dict[temp_data[0]] += int(temp_data[1])

    with open(report_file_name, "a") as report_file:
        report_file.write(f"{'supply'},{data_dict['supply']}\n")
        report_file.write(f"{'buy'},{data_dict['buy']}\n")
        report_file.write(
            f"result,{data_dict['supply'] - data_dict['buy']}\n"
        )
