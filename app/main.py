def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dct = {}
    with open(data_file_name, "r") as input_file:
        for line in input_file:
            action, amount = line.split(",")
            if data_dct.get(action):
                data_dct[action] += int(amount)
            else:
                data_dct[action] = int(amount)

    with open(report_file_name, "w") as output_file:
        output_file.write(f"supply,{data_dct["supply"]}\n")
        output_file.write(f"buy,{data_dct["buy"]}\n")
        output_file.write(
            f"result,{data_dct["supply"] - data_dct["buy"]}\n"
        )
        output_file.write("")
