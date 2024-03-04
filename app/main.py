def create_report(data_file_name: str, report_file_name: str):
    supply = []
    buy = []
    with open(data_file_name, "r") as f:
        for line in f.readlines():
            if line.startswith("supply"):
                supply.append(int(line.split(",", 1)[1]))
            if line.startswith("buy"):
                buy.append(int(line.split(",", 1)[1]))

    with open(report_file_name, "w") as f:
        f.write(f"supply,{sum(supply)}\n"
                f"buy,{sum(buy)}\n"
                f"result,{sum(supply) - sum(buy)}\n")
