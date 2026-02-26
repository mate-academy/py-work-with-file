def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    sum_supply = 0
    sum_buy = 0

    with open(data_file_name, "r") as f:
        for i in f:
            i = i.strip()
            name, amount = i.split(",")
            if name == "supply":
                sum_supply += int(amount)
            elif name == "buy":
                sum_buy += int(amount)

    with open(report_file_name, "w") as r:
        r.write(f"supply,{sum_supply}\n")
        r.write(f"buy,{sum_buy}\n")
        r.write(f"result,{sum_supply - sum_buy}\n")
