def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")

    recoded_data = {"supply": 0, "buy": 0}

    for line in data_file:
        if line is not None:
            data = line.split(",")
            recoded_data[data[0]] += int(data[1])

    data_file.close()

    record_file = open(report_file_name, "w")
    record_file.write(
        f"supply,{recoded_data['supply']}\n"
        f"buy,{recoded_data['buy']}\n"
        f"result,{recoded_data['supply'] - recoded_data['buy']}\n"
    )
    record_file.close()
