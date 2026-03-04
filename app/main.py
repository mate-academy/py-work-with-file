def create_report(data_file_name: str, report_file_name: str) -> str:

    with open(data_file_name, 'r') as data_file:
        report_dict = {}
        for line in data_file:
            key, value = line.strip().split(',')
            report_dict[key] = report_dict.get(key, 0) + int(value)

    with open(report_file_name, 'a') as report_file:
        for key, value in report_dict.items():
            report_file.write(f"{key},{value}\n")

    return report_file_name
