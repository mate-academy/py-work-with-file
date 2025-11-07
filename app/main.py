def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    fd = open(data_file_name, "r")
    for line in fd:
        op_type, amount = line.split(",")
        if op_type == "supply":
            supply += int(amount)
        elif op_type == "buy":
            buy += int(amount)
    fd.close()

    fd = open(report_file_name, "w")
    fd.write(f"supply,{supply}\n")
    fd.write(f"buy,{buy}\n")
    fd.write(f"result,{supply - buy}\n")
    fd.close()
