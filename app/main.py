def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    data_file = open(data_file_name, "r")
    data_dict = {"supply": 0, "buy": 0}

    for line in data_file:
        key, value = line.strip().split(",")
        data_dict[key] += int(value)

    data_file.close()

    report_file = open(report_file_name, "w")

    report_file.write("supply," + str(data_dict["supply"]) + "\n")
    report_file.write("buy," + str(data_dict["buy"]) + "\n")
    report_file.write(
        "result," + str(data_dict["supply"] - data_dict["buy"]) + "\n"
    )

    report_file.close()
