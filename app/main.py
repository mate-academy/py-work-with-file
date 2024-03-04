def create_report(data_file_name: str,
                  report_file_name: str):
    sum_of_supply = 0
    sum_of_buy = 0
    with open(data_file_name, "r") as file_out:
        for line in file_out.readlines():
            if not line:
                continue

            operation, income = line.split(",")

            if operation == "supply":
                sum_of_supply += int(income)
            if operation == "buy":
                sum_of_buy += int(income)

    with open(report_file_name, "w") as file_in:
        file_in.write(f"supply,{sum_of_supply}\n")
        file_in.write(f"buy,{sum_of_buy}\n")
        file_in.write(f"result,{sum_of_supply - sum_of_buy}\n")
