def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as f:
        file_list = f.readlines()

    result_dict = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }

    for line in file_list:
        operation_type, amount = line.split(",")
        result_dict[operation_type] += int(amount)

    result_dict["result"] = result_dict["supply"] - result_dict["buy"]

    with open(report_file_name, "w") as f:
        for key, value in result_dict.items():
            f.writelines(f"{key},{value}\n")
