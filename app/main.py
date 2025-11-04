def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    file = open(data_file_name, 'r')
    for line in file:
        if not line:
            continue
        operation, amount = line.split(',')
        amount = int(amount)
        if operation == "supply":
            supply += amount
        else:
            buy += amount
    file.close()
    report_file = open(report_file_name, 'w')
    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{supply - buy}\n")
    report_file.close()




