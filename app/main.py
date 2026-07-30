def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    data_dict = {"supply": 0, "buy": 0}
    data_file = open(data_file_name)

    for line in data_file:
        if line == "\n":
            break
        field, value = line.split(",")
        data_dict[field] += int(value)

    data_file.close()

    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{data_dict['supply']}\n")
    report_file.write(f"buy,{data_dict['buy']}\n")
    report_file.write(f"result,{data_dict['supply'] - data_dict['buy']}\n")
    report_file.close()
