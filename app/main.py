def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f:
        all_suppliers = 0
        all_bought = 0

        for line in f:
            line = line.strip()
            if not line:
                continue
            item, quantity = line.split(",")
            if item == "supply":
                all_suppliers += int(quantity)
            if item == "buy":
                all_bought += int(quantity)

        result = all_suppliers - all_bought

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{all_suppliers}\n"
            f"buy,{all_bought}\n"
            f"result,{result}\n"
        )
