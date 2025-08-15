import csv


def create_report(data_file_name: str, report_file_name: str):
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            op, value = row[0], row[1]
            amount = int(value)
            if op == "supply":
                total_supply += amount
            elif op == "buy":
                total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w", encoding="utf-8", newline="") as out:
        out.write(f"supply,{total_supply}\n")
        out.write(f"buy,{total_buy}\n")
        out.write(f"result,{result}\n")
