def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {}
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        for line in data_file.readlines():
            key, value = line.split(",")
            value = int(value)
            if key in data_dict:
                data_dict[key] += value
            else:
                data_dict[key] = value
        supply = data_dict["supply"]
        buy = data_dict["buy"]
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_value = data_dict["supply"] - data_dict["buy"]
        report_file.write(f"result,{report_value}\n")
