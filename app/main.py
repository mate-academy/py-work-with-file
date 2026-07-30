def create_report(data_file_name: str, report_file_name: str) -> None:
    file_to_read = open(data_file_name)
    data_from_file = file_to_read.readlines()
    result_dict = {}
    for i in data_from_file:
        key = i.split(",")[0]
        value = i.split(",")[1].rstrip("\n")
        if key in result_dict:
            result_dict[key] += int(value)
        else:
            result_dict[key] = int(value)
    file_to_read.close()

    result_file = open(report_file_name, "a")
    supply_value = result_dict["supply"]
    buy_value = result_dict["buy"]
    result_value = supply_value - buy_value

    result_file.write("supply," + str(supply_value) + "\n")
    result_file.write("buy," + str(buy_value) + "\n")
    result_file.write("result," + str(result_value) + "\n")
    result_file.close()
