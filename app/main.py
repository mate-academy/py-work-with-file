import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_buy = {"supply": 0, "buy": 0}
    with (open(data_file_name, "r") as cvs_file,
          open(report_file_name, "w") as report_file):
        reader = csv.reader(cvs_file)
        #writer = csv.writer(report_file)
        for row in reader:
            if row[0] == "supply":
                supply_buy["supply"] += int(row[1])
            if row[0] == "buy":
                supply_buy["buy"] += int(row[1])
        # report_result = [["supply", supply_buy["supply"]],
        #                  ["buy", supply_buy["buy"]],
        #                  ["result", supply_buy["supply"] - supply_buy["buy"]]]
        # for row in report_result:
        #     writer.writerow(row)
        report_file.write(f"supply,{supply_buy["supply"]}\n")
        report_file.write(f"buy,{supply_buy["buy"]}\n")
        report_file.write(f"result,"
                          f"{supply_buy["supply"] - supply_buy["buy"]}\n")
