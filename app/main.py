def read_report_from_file(data_file_name: str) -> dict:
    file_read = open(f"{data_file_name}")
    report = dict()
    for line in file_read:
        key, value = line.split(",")
        if key not in report:
            report[key] = int(value)
        else:
            report[key] += int(value)
    report["result"] = report["supply"] - report["buy"]
    file_read.close()
    return report


def write_report_to_file(report: dict, report_file_name: str) -> None:
    file_write = open(f"{report_file_name}", "w")
    for key in ["supply", "buy", "result"]:
        file_write.write(f"{key},{report[key]}\n")
    file_write.close()


def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    report = read_report_from_file(data_file_name)
    write_report_to_file(report, report_file_name)
