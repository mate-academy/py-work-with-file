from pathlib import Path


def create_report(data_file_name: str, report_file_name: str) -> None:
    base_path = Path(__file__).parent.parent

    data_file = open(base_path / data_file_name, "r")
    report_file = open(report_file_name, "w")
    report = {}

    for line in data_file:
        line = line.rstrip("\n").split(",")

        if line[0] not in report:
            report[line[0]] = int(line[1])
        else:
            report[line[0]] += int(line[1])

    report_file.write(f"supply,{report['supply']}\n"
                      f"buy,{report['buy']}\n"
                      f"result,{report['supply'] - report['buy']}\n")

    data_file.close()
    report_file.close()
