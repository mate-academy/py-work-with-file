# write your code here
def create_report(data_file_name: str, report_file_name: str) -> any:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as file_in:
        for line in file_in:
            line = line.strip()
            if not line:
                continue

            operation, amount_str = line.split(",")
            amount = int(amount_str)

            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w") as file_out:
        file_out.write(f"supply,{total_supply}\n")
        file_out.write(f"buy,{total_buy}\n")
        file_out.write(f"result,{result}\n")
