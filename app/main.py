def create_report(
    data_file_name: str, report_file_name: str
) -> None:

    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as data_file:
        lines = data_file.readlines()

        for line in lines:
            operation, amount = line.strip().split(",")
            amount = int(amount)

            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount

    report = [
        f"supply,{total_supply}",
        f"buy,{total_buy}",
        f"result,{total_supply - total_buy}"
    ]

    with open(report_file_name, mode="w") as report_file:
        report_file.write("\n".join(report) + "\n")
