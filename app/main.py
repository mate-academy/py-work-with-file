# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data,
          open(report_file_name, "w") as report):
        report_dict = {
            "supply": 0,
            "buy": 0,
            "result": 0,
        }

        for line in data:
            operation, amount = line.split(",")
            amount = amount.replace("\n", "")
            report_dict[operation] += int(amount)

        report_dict["result"] = report_dict["supply"] - report_dict["buy"]

        for operation, amount in report_dict.items():
            report.write(",".join((operation, str(amount))) + "\n")
