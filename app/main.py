import csv


def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    """
    Create a report from the given data file and save it to the specified
    report file.

    Args:
        data_file_name (str): The name of the CSV file containing the data.

        report_file_name (str): The name of the CSV file where the report
        will be saved.
    """
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        data = csv.reader(data_file)
        for row in data:
            if row[0].lower() == "supply":
                supply += int(row[1])
            elif row[0].lower() == "buy":
                buy += int(row[1])

    with open(report_file_name, "w") as report_file:
        report_writer = csv.writer(report_file)
        report_writer.writerow(["supply", supply])
        report_writer.writerow(["buy", buy])
        report_writer.writerow(["result", supply - buy])
