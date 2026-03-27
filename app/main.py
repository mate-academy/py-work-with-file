def create_report(data_file_name: str, report_file_name: str) -> None:
    input_file = open(data_file_name)
    lines = input_file.readlines()
    input_file.close()
    supply = []
    buy = []
    for i in lines:
        operation, amount = i.strip().split(",")
        if operation == "supply":
            supply.append(int(amount))
        else:
            buy.append(int(amount))
    output_file = open(report_file_name, mode="w")
    output_file.write(f"supply,{sum(supply)}\n")
    output_file.write(f"buy,{sum(buy)}\n")
    output_file.write(f"result,{sum(supply) - sum(buy)}\n")
    output_file.close()
