def create_report(data_file_name: str, report_file_name: str) -> None:
    operation_index = 0
    quantity_index = 1
    total_supplied = 0
    total_bought = 0

    with open(data_file_name, "r") as f:
        for line in f:
            if line.split(",")[operation_index] == "buy":
                total_bought += line.split()[quantity_index]
            if line.split(",")[operation_index] == "supply":
                total_supplied += line.split()[quantity_index]

    with open(report_file_name, "w") as f:
        f.write("supply," + str(total_supplied))
        f.write("buy," + str(total_bought))
        f.write("result," + str(total_supplied - total_bought))
