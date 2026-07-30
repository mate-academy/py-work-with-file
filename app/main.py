def create_report(data_file_name: str, report_file_name: str):
    report = dict()
    with open(data_file_name) as file_in:
        for line in file_in:
            key, value = line[:-1].split(",")
            if key in report:
                report[key] += int(value)
            else:
                report[key] = int(value)
    with open(report_file_name, "w") as file_out:
        file_out.write(f"supply,{str(report['supply'])}\n")
        file_out.write(f"buy,{str(report['buy'])}\n")
        file_out.write(f"result,{report['supply'] - report['buy']}\n")
