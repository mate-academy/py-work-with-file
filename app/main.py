def create_report(data_file_name: str, report_file_name: str):

    with open(data_file_name, "r") as data:
        trade = data.readlines()

        supply = sum(int(line.split(",")[1]) for line in trade
                     if line.split(",")[0] == "supply")

        buy = sum(int(line.split(",")[1]) for line in trade
                  if line.split(",")[0] == "buy")

        with open(report_file_name, "w") as report:
            report.write(f"supply,{supply}\n"
                         f"buy,{buy}\n"
                         f"result,{supply - buy}\n")
