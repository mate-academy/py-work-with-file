# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, "r") as file_in:
        data = file_in.readlines()
        for line in data:
            action, amount = line.split(",")
            if action == "supply":
                total_supply += int(amount)
            if action == "buy":
                total_buy += int(amount)

    with open(report_file_name, "w+") as file_out:
        file_out.write(f"supply,{total_supply}\n")
        file_out.write(f"buy,{total_buy}\n")
        file_out.write(f"result,{total_supply - total_buy}\n")
