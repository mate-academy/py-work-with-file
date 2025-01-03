def create_report(data_file_name: str, report_file_name: str) -> None:
    dict_values = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            f_key, f_value = line.split(",")
            dict_values[f_key] += int(f_value)

    with open(report_file_name, "a") as report:
        report.write(f"supply,{dict_values["supply"]}\n")
        report.write(f"buy,{dict_values["buy"]}\n")
        report.write(f"result,{dict_values["supply"] - dict_values["buy"]}\n")
