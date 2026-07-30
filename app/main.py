def create_report(date_file_name: str, report_file_name: str) -> None:
    date_file = open(date_file_name, "r")
    result_dict = {}
    for line in date_file.readlines():
        key, value = line.split(",")
        if key not in result_dict:
            result_dict[key] = int(value)
        else:
            result_dict[key] += int(value)
    result_dict["result"] = result_dict.get("supply") - result_dict.get("buy")
    report_file = open(report_file_name, "w")
    for key in ["supply", "buy", "result"]:
        report_file.write(f"{key},{result_dict[key]}\n")
    report_file.close()
    date_file.close()
