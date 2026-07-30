import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {}
    with open(data_file_name, newline="") as csv_file:
        report_file = csv.reader(csv_file)
        for row in report_file:
            if row[0] not in report_dict:
                new_line = {row[0]: row[1]}
                report_dict.update(new_line)
            else:
                report_dict[row[0]] = int(report_dict[row[0]]) + int(row[1])
        result_line = int(report_dict["supply"]) - int(report_dict["buy"])
        report_dict["result"] = result_line
    new_file = open(report_file_name, "w")
    new_file.write(f"supply,{report_dict['supply']}\n")
    new_file.write(f"buy,{report_dict['buy']}\n")
    new_file.write(f"result,{report_dict['result']}\n")
    new_file.close()
