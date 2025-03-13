def convert_string(string: str) -> int | float:
    try:
        return int(string)
    except ValueError:
        try:
            return float(string)
        except ValueError:
            return 0


def create_report(data_file_name: str, report_file_name: str) -> None:
    file_data = {"supply": "0", "buy": "0", "result": "0"}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            key, value = line.strip().split(",")
            if key in file_data:
                dict_value = file_data[key]
                file_data[key] = str(
                    convert_string(dict_value) + convert_string(value)
                )
                file_data["result"] = str(
                    convert_string(file_data["supply"])
                    - convert_string(file_data["buy"])
                )
            else:
                file_data[key] = value

    with open(report_file_name, "w") as report_file:
        for key, value in file_data.items():
            report = f"{key},{value}\n"
            report_file.write(report)

    data_file.close()
    report_file.close()
