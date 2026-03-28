import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            if line:
                oper_type, amount = line

                amount = int(amount)

                if oper_type == "supply":
                    total_supply += amount
                elif oper_type == "buy":
                    total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w") as csv_write_file:
        csv_write_file.write(f"supply,{total_supply}\n")
        csv_write_file.write(f"buy,{total_buy}\n")
        csv_write_file.write(f"result,{result}\n")
