import csv


def create_report(data_file_name: str, report_file_name: str) -> None:

    supply = 0
    buy = 0

    with open(data_file_name, "r") as file_read:
        csv_reader = csv.reader(file_read)

        for data in csv_reader:

            operant = data[0]
            amount = int(data[1])

            if operant == "supply":
                supply += amount
            elif operant == "buy":
                buy += amount

        result = supply - buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
