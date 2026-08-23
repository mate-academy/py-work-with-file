def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = dict()
    with (open(data_file_name, "r") as f):

        for line in f:
            key, amount = line.split(",")
            report_dict[key] = report_dict.get(key, 0) + int(amount)

    report_dict["result"] = report_dict["supply"] - report_dict["buy"]

    with open(report_file_name, "w") as f:
        freez_order = ("supply", "buy", "result")
        for key in freez_order:
            f.write(f"{key},{report_dict[key]}\n")
