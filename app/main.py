def create_report(data_file_name: str, report_file_name: str) -> None:
    dict_with_data = {"supply": 0, "buy": 0}
    with (open(data_file_name) as data_file,
          open(report_file_name, "w") as report_file):
        for line in data_file:
            key, value = line.strip().split(",")
            dict_with_data[key] += int(value)

        result = dict_with_data["supply"] - dict_with_data["buy"]

        report_file.write(f"supply,{dict_with_data['supply']}\n")
        report_file.write(f"buy,{dict_with_data['buy']}\n")
        report_file.write(f"result,{result}\n")
