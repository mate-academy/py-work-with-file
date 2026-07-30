def create_report(date_file_name: str, report_file_name: str) -> None:
    date_file = open(date_file_name, "r")
    report_file = open(report_file_name, "w")
    result_dict = dict()
    for line in date_file.readlines():
        name, quantity = line.split(",")
        if name not in result_dict:
            result_dict[name] = int(quantity)
        else:
            result_dict[name] += int(quantity)
    result_dict["result"] = result_dict.get("supply") - result_dict.get("buy")
    for key in ["supply", "buy", "result"]:
        report_file.write(f"{key},{result_dict[key]}\n")  # NOQA E231
    report_file.close()
    date_file.close()
