import csv


def create_report(data_file_name: str, report_file_name: str) -> str:
    report_dict = {}
    with open(data_file_name, "r") as file1:
        reader = csv.reader(file1)
        for line in reader:
            if line[0] not in report_dict:
                report_dict[line[0]] = int(line[1])
            else:
                report_dict[line[0]] += int(line[1])

    with open(report_file_name, "w") as file2:
        file2.write(f'supply,{report_dict["supply"]}\n')
        file2.write(f'buy,{report_dict["buy"]}\n')
        file2.write(f'result,{report_dict["supply"] - report_dict["buy"]}\n')

    return report_file_name
