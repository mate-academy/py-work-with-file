def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    data = open(data_file_name)
    report = open(report_file_name, "w")

    supply_amount = 0
    buying_amount = 0

    for line in data:
        if line.startswith("supply"):
            supply_amount += int(
                line.replace(
                    "supply,",
                    ""
                )
            )
        if line.startswith("buy"):
            buying_amount += int(
                line.replace(
                    "buy,",
                    ""
                )
            )

    report.write(
        "supply," + str(supply_amount) + "\n"
        "buy," + str(buying_amount) + "\n"
        "result," + str(supply_amount - buying_amount) + "\n"
    )
