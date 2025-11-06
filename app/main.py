def create_report(data_file_name: str, report_file_name: str) -> None:
    file_to_read = open(data_file_name, mode="r")
    report = {}
    for line in file_to_read:
        line_list = line.split(",")
        key = line_list[0]
        value = int(line_list[1])
        report[key] = report.get(key, 0) + value
    file_to_read.close()

    report["result"] = report.get("supply", 0) - report.get("buy", 0)

    file_to_write = open(report_file_name, mode="w")

    file_to_write.write(f"supply,{report.get("supply")}\n")
    file_to_write.write(f"buy,{report.get("buy")}\n")
    file_to_write.write(f"result,{report.get("result")}\n")
    file_to_write.close()
