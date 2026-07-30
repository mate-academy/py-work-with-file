def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as source:
        to_sort = source.read()

    report = {}
    for line in to_sort.rstrip().split("\n"):
        name, amount = line.split(",")
        if report.get(name):
            report[name] += int(amount)
        else:
            report[name] = int(amount)
    with open(report_file_name, "w") as destination:

        destination.write(f"supply,{report['supply']}\n")
        destination.write(f"buy,{report['buy']}\n")
        destination.write(f"result,{report['supply'] - report['buy']}\n")
