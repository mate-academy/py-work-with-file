
def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as out_file,
        open(report_file_name, "a") as in_file
    ):
        total_supply = 0
        total_buy = 0
        for line in out_file:
            operation, amount = line.split(",")
            total_supply += int(amount) if operation == "supply" else + 0
            total_buy += int(amount) if operation == "buy" else + 0
        in_file.write(f"supply,{total_supply}\n")
        in_file.write(f"buy,{total_buy}\n")
        in_file.write(f"result,{total_supply - total_buy}\n")
