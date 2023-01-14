def create_report(data_file_name: str, report_file_name: str) -> None:
    operation_index = 0
    quantity_index = 1
    total_supplied = 0
    total_bought = 0

    with open(data_file_name, "r") as f:
        for line in f:
            if line.split(",")[operation_index] == "buy":
                total_bought += int(line.split(",")[quantity_index])
            if line.split(",")[operation_index] == "supply":
                total_supplied += int(line.split(",")[quantity_index])

    with open(report_file_name, "w") as f:
        f.write(f"supply,{total_supplied}\n")
        f.write(f"buy,{total_bought}\n")
        f.write(f"result,{total_supplied - total_bought}\n")
