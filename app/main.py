def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        data_dict = {"supply": 0, "buy": 0}
        while True:
            cur_row = data_file.readline()
            if not cur_row:
                break
            operation, amount = cur_row.split(",")
            if operation in data_dict:
                data_dict[operation] += int(amount)
        data_dict["result"] = data_dict["supply"] - data_dict["buy"]
    with open(report_file_name, "w") as report_file:
        for key, value in data_dict.items():
            report_file.write(",".join([key, str(value)]) + "\n")
