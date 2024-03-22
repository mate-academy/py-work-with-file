import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file_csvfile,
        open(report_file_name, "w") as report_csvfile,
    ):
        csvreader = csv.reader(data_file_csvfile)

        total_operations_type_amount = {}

        for [operations_type, amount] in csvreader:
            operations_type_amount = (
                total_operations_type_amount.get(operations_type) or 0
            )

            total_operations_type_amount[operations_type] = (
                operations_type_amount + int(amount)
            )

        writer = csv.writer(report_csvfile)

        writer.writerow(["supply", total_operations_type_amount["supply"]])
        writer.writerow(["buy", total_operations_type_amount["buy"]])

        writer.writerow(
            [
                "result",
                total_operations_type_amount["supply"]
                - total_operations_type_amount["buy"],
            ]
        )
