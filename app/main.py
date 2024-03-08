import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = {"supply": 0, "buy": 0}
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        csv_reader = csv.reader(file_in)
        for row in csv_reader:
            if row:
                row_type, amount = row
                if row_type in total_supply:
                    total_supply[row_type] += int(amount)
        supply = total_supply["supply"]
        buy = total_supply["buy"]
        result = supply - buy
        file_out.write(f"supply,{supply}\n")
        file_out.write(f"buy,{buy}\n")
        file_out.write(f"result,{result}\n")


create_report("apples.csv", "new_file2.csv")