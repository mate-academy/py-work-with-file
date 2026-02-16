def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply_total = 0
    buy_total = 0

    file_in = open(data_file_name, "r")

    for line in file_in:
        if "," in line:
            parts = line.split(",")

            operation = parts[0]

            amount = int(parts[1])

            if operation == "supply":
                supply_total += amount
            if operation == "buy":
                buy_total += amount

    file_in.close()

    result = supply_total - buy_total

    file_out = open(report_file_name, "w")

    file_out.write("supply," + str(supply_total) + "\n")
    file_out.write("buy," + str(buy_total) + "\n")
    file_out.write("result," + str(result) + "\n")

    file_out.close()
