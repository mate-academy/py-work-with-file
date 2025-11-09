def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue
            parts = cleaned_line.split(",")
            if len(parts) == 2:
                operation = parts[0]
                if operation in totals:
                    try:
                        totals[operation] += int(parts[1])
                    except ValueError:
                        continue

    result = totals["supply"] - totals["buy"]

    with open(report_file_name, "w") as report_file:
        report_file.write("supply," + str(totals["supply"]) + "\n")
        report_file.write("buy," + str(totals["buy"]) + "\n")
        report_file.write("result," + str(result) + "\n")
