import csv


def create_report(data_file_name: str, report_file_name: str) -> any:
    supply = 0
    buy = 0

    with open(data_file_name, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue

            operation, amount = row
            if operation == "supply":
                supply += int(amount)
            elif operation == "buy":
                buy += int(amount)

    result = supply - buy

    with open(report_file_name, mode="w", encoding="utf-8") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")


if __name__ == "__main__":
    files = ["apples.csv", "bananas.csv", "grapes.csv", "oranges.csv"]

    for filename in files:
        report_name = f"report_{filename}"
        create_report(filename, report_name)
        print(f"Raport dla {filename} został utworzony jako {report_name}")
