def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {"supply": 0, "buy": 0}
    with (open(data_file_name, "r") as data,
          open(report_file_name, "w") as report):
        for line in data:
            data_dict[line.split(",")[0]] += int(line.split(",")[1])
        report.write(f"supply,{data_dict["supply"]}\n"
                     f"buy,{data_dict["buy"]}\n"
                     f"result,{data_dict["supply"] - data_dict["buy"]}\n")
