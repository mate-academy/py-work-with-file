def create_report(data_file_name: str, report_file_name: str) -> None:
    p1 = open(data_file_name, "r")

    sum_buy = 0
    sum_supply = 0
    for line in p1:
        if line.strip():
            parts = line.split(",")
            operation_type = parts[0].strip()
            amount = int(parts[1].strip())

            if operation_type == "supply":
                sum_supply += amount
            elif operation_type == "buy":
                sum_buy += amount

    result = sum_supply - sum_buy

    p2 = open(report_file_name, "w")

    p2.write("supply," + str(sum_supply) + "\n")
    p2.write("buy," + str(sum_buy) + "\n")
    p2.write("result," + str(result) + "\n")
    p2.close()
