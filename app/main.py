def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data_file:
        for row in data_file:
            row = row.strip()
            operation, amount = row.split(",")
            totals[operation] += int(amount)

    totals["result"] = totals["supply"] - totals["buy"]

    with open(report_file_name, "w") as report_file:
        for key, value in totals.items():
            report_file.write(f"{key},{value}\n")

    data_file.close()
    report_file.close()


if __name__ == "__main__":
    create_report("../apples.csv", "../report.csv")
