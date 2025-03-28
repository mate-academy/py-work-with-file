def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dicts = []
    with open(data_file_name) as data_file:
        for line in data_file:
            try:
                operation, amount = line.strip().split(",")
            except Exception:
                break
            if not report_dicts:
                report_dicts.append({operation: int(amount)})
                continue
            for i, item in enumerate(report_dicts):
                if operation in item:
                    report_dicts[i][operation] += int(amount)
                    break
                if i == len(report_dicts) - 1:
                    report_dicts.append({operation: int(amount)})
                    break

    report_csv = []
    for item in report_dicts:
        operation = list(item.keys())[0]
        if operation == "supply":
            supply = item[operation]
            report_csv.append(f"{operation},{item[operation]}\n")
        else:
            buy = item[operation]

    report_csv.append(f"buy,{buy}\n")
    report_csv.append(f"result,{supply - buy}\n")

    with open(report_file_name, "w") as report_file:
        report_file.writelines(report_csv)
