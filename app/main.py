def create_report(data_file_name: str, report_file_name: str) -> None:
    data_report = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file:
        rows = file.readlines()

        for row in rows:
            if row:
                operation, value = row.strip().split(",")
                if operation == "supply":
                    data_report["supply"] += int(value)
                elif operation == "buy":
                    data_report["buy"] += int(value)

    data_report["result"] = data_report["supply"] - data_report["buy"]

    with open(report_file_name, "w") as report:
        for key, value in data_report.items():
            report.write(f"{key},{value}\n")
