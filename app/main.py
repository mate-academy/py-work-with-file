def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        result = {
            "buy": 0,
            "supply": 0
        }

        list_file_in = file_in.read().split()

        for data_file in list_file_in:
            corrected_data_file = data_file.split(",")
            result[corrected_data_file[0]] += int(corrected_data_file[1])

        file_out.write(f"supply, {result["supply"]}\n"
                       f"buy, {result["buy"]}\n"
                       f"result, {result["supply"] - result["buy"]}\n")
