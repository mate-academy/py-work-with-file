import os


def create_report(data_file_name: str, report_file_name: str):
    supply_total = 0
    buy_total = 0

    data_path = os.path.join('tests', data_file_name)
    report_path = os.path.join('tests', report_file_name)

    with open(data_file_name, 'r') as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue
            operation, value = line.split(',')
            value = int(value)
            if operation == "supply":
                supply_total += value
            elif operation == "buy":
                buy_total += value
    result = supply_total - buy_total

    with open(report_file_name, 'w') as report_file:
        report_file.write(f"supply, {supply_total}\n")
        report_file.write(f"buy, {buy_total}\n")
        report_file.write(f"result, {result}\n")

