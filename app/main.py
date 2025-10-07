def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dictionary = {
        "supply": 0,
        "buy": 0
    }
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()

            if not line:
                continue

            operation, amount_str = line.split(",", 1)
            amount = int(amount_str)
            if operation == "buy":
                data_dictionary["buy"] += amount
            if operation == "supply":
                data_dictionary["supply"] += amount

    supply = data_dictionary["supply"]
    buy = data_dictionary["buy"]
    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")

