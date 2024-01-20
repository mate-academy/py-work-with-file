def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file_in:
        for line in file_in:
            action, amount = line.split(",")
            if action == "supply":
                supply += int(amount)
            else:
                buy += int(amount)

    with open(report_file_name, "w") as file_out:
        file_out.write("supply," + str(supply) + "\n")
        file_out.write("buy," + str(buy) + "\n")
        file_out.write("result," + str(supply - buy) + "\n")
