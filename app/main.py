def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f:
        data_read = f.read()
        data_read = data_read.split()
        data_read_result = [el.split(",") for el in data_read]
    supply_count = 0
    buy_count = 0
    for i in data_read_result:
        if "supply" in i:
            supply_count += int(i[1])
        if "buy" in i:
            buy_count += int(i[1])
    with open(report_file_name, "w") as b:
        b.write(f"supply,{supply_count}\n")
        b.write(f"buy,{buy_count}\n")
        b.write(f"result,{supply_count-buy_count}\n")
