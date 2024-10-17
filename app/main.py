def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_ttl = 0
    buy_ttl = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if not line.strip():
                continue
            lst = line.strip().split(",")
            amount = int(lst[1])
            if lst[0] == "supply":
                supply_ttl += amount
            if lst[0] == "buy":
                buy_ttl += amount

        result = supply_ttl - buy_ttl

    with open(report_file_name, "w") as write_file:
        write_file.write(f"supply, {supply_ttl}\n")
        write_file.write(f"buy, {buy_ttl}\n")
        write_file.write(f"result, {result}\n")
