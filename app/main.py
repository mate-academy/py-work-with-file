def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {}
    with open(data_file_name, "r") as file_read:
        data = file_read.read().split("\n")
        for line in data:
            if line != "":
                text = line.split(",")
                if text[0] in report.keys():
                    report[text[0]] += int(text[1])
                else:
                    report[text[0]] = int(text[1])

    with open(report_file_name, "w") as file_report:
        file_report.write(f"supply,{report['supply']}\n")
        file_report.write(f"buy,{report['buy']}\n")
        file_report.write(f"result,{(report['supply'] - report['buy'])}\n")
