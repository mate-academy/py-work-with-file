def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    data_dict = {
        "supply": 0,
        "buy": 0,
        "result": 0

    }
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "a") as report_file):

        for line in data_file:
            if line:
                operation_type, amount = line.split(",")
                data_dict[operation_type] += int(amount)
        data_dict["result"] = data_dict["supply"] - data_dict["buy"]
        for key, value in data_dict.items():
            report_file.write(f"{key},{value}\n")
