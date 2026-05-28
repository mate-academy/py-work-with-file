import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name,
              mode="r",
              newline="",
              encoding="utf-8"
              ) as infile:
        reader = csv.reader(infile)
        for row in reader:
            if not row:
                continue
            operation_type, amount_str = row[0], row[1]
            amount = int(amount_str)
            if operation_type in totals:
                totals[operation_type] += amount

    result = totals["supply"] - totals["buy"]
    with open(report_file_name,
              mode="w",
              newline="",
              encoding="utf-8"
              ) as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["supply", totals["supply"]])
        writer.writerow(["buy", totals["buy"]])
        writer.writerow(["result", result])
