def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as input_file,
          open(report_file_name, "w") as output_file):
        result_dict_report = {
            "supply": 0,
            "buy": 0,
            "result": 0
        }

        for line in input_file:
            key, value = line.split(",")
            result_dict_report[key] += int(value.strip())

        result_dict_report["result"] = (
            result_dict_report["supply"] - result_dict_report["buy"]
        )

        for key, value in result_dict_report.items():
            output_file.write(f"{key},{value}\n")
