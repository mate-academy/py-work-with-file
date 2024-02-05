def create_report(data_file_name: str, report_file_name: str) -> None:

    with (open(data_file_name, "r") as source_file,
          open(report_file_name, "w") as destination_file):
        data_dict = {
            "supply": 0,
            "buy": 0,
        }
        for row in source_file.readlines():
            operation, amount = row.split(",")
            data_dict[operation] += int(amount)

        data_dict["result"] = data_dict["supply"] - data_dict["buy"]

        destination_file.writelines(
            [f"{key},{value}\n" for key, value in data_dict.items()]
        )
