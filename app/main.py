def create_report(data_file_name: str, report_file_name: str) -> None:
    summary = {"supply": 0,
               "buy": 0,
               "result": 0}

    with (open(f"{data_file_name}", "r") as source_file,
          open(f"{report_file_name}", "w") as report_file):
        for line in source_file:
            try:
                line = line.split(",")
                summary[line[0]] += int(line[1].replace("\n", ""))
            except ValueError as e:
                print(f"Source file contains empty lines "
                      f"or invalid values:\n{e}")

        report_file.write(f"supply,{summary['supply']}\n"
                          f"buy,{summary['buy']}\n"
                          f"result,{summary['supply'] - summary['buy']}")
