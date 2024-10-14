def create_report(data_file_name: str, report_file_name: str) -> None:
    dict_of_data = {}

    with open(data_file_name) as f:
        for line in f:
            value, amount = line.rstrip("\n").split(",")
            if value not in dict_of_data:
                dict_of_data[value] = int(amount)
            else:
                dict_of_data[value] += int(amount)

    result = dict_of_data["supply"] - dict_of_data["buy"]

    with open(report_file_name, "w") as f:
        f.write(f"supply,{dict_of_data["supply"]}\n")  # noqa: E231
        f.write(f"buy,{dict_of_data["buy"]}\n")  # noqa: E231
        f.write(f"result,{result}\n")  # noqa: E231
