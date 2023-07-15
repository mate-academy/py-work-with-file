def create_report(data_file_name: str, report_file_name: str) -> None:
    total_buy = 0
    total_supply = 0

    with open(data_file_name, "r") as file_in:
        for item in file_in:
            key, value = item.strip().split(",")
            if key == "buy":
                total_buy += int(value)
            elif key == "supply":
                total_supply += int(value)

    with open(report_file_name, "w") as file_output:
        file_output.write(f"supply,{total_supply}\n")
        file_output.write(f"buy,{total_buy}\n")
        file_output.write(f"result,{total_supply - total_buy}\n")
