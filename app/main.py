def create_report(data_file_name: str,
                  report_file_name: str
                  ) -> None:

    file_info = {"supply": 0, "buy": 0, "result": 0}

    with (open(data_file_name, "r") as data,
          open(report_file_name, "w") as report):

        for line in data.readlines():
            line = line.split(",")
            file_info[line[0]] += int(line[1])
        file_info["result"] = file_info["supply"] - file_info["buy"]
        for key, value in file_info.items():
            report.write(f"{key},{value}\n")
