import os


def create_report(data_file_name: str, report_file_name: str):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    data_path = os.path.join(BASE_DIR, data_file_name)
    report_path = os.path.join(BASE_DIR, report_file_name)

    with open(data_path, "r", encoding="utf-8") as data_file, \
         open(report_path, "w", encoding="utf-8") as report_file:

        report = {
            "supply": 0,
            "buy": 0
        }

        for line in data_file:
            if not line.strip():
                continue

            operation, amount = line.strip().split(",")
            report[operation] += int(amount)

        result = report["supply"] - report["buy"]

        report_file.write(f"supply,{report['supply']}\n")
        report_file.write(f"buy,{report['buy']}\n")
        report_file.write(f"result,{result}\n")