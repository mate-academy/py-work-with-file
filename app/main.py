def create_report(data_file_name: str, report_file_name: str) -> None:
    sum_supply = 0
    sum_buy = 0
    with open(data_file_name, "r") as data_in:
        while True:
            line = data_in.readline()
            if not line:
                break
            operation_type = line.split(",")[0]
            amount = int(line.split(",")[1])
            if operation_type == "supply":
                sum_supply += amount
            if operation_type == "buy":
                sum_buy += amount
    with open(report_file_name, "w") as data_out:
        data_out.write(f"supply,{sum_supply}\n")
        data_out.write(f"buy,{sum_buy}\n")
        data_out.write(f"result,{sum_supply - sum_buy}\n")
