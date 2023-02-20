def create_report(data: str, report: str) -> None:
    with open(data, "r") as f_d, open(report, "w") as f_r:
        supply = []
        buy = []
        for line in f_d:
            data_lines = line.split(",")
            if data_lines[0] == "supply":
                supply.append(int(data_lines[1]))
            elif data_lines[0] == "buy":
                buy.append(int(data_lines[1]))
        result = sum(supply) - sum(buy)
        f_r.write(f"supply,{sum(supply)}\n")
        f_r.write(f"buy,{sum(buy)}\n")
        f_r.write(f"result,{result}\n")
