import csv


def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as f:
        rows = csv.reader(f)
        supply = 0
        buy = 0
        for row in rows:
            if row:
                operation = row[0]
                amount = int(row[1])

                if operation == "supply":
                    supply += amount
                else:
                    buy += amount
    result = supply - buy

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")
