def create_report(data_file_name: str, report_file_name: str):
    with open(f"../{data_file_name}", 'r') as f,\
            open(report_file_name, "w") as rep_file:
        buy = []
        supply = []
        for item in sorted(f.readlines()):
            key = item.strip("\n").split(",")[0]
            value = int(item.strip("\n").split(",")[1])
            if key == "buy":
                buy.append(value)
            else:
                supply.append(value)
        rep_file.write(f"supply,{sum(supply)}\n")
        rep_file.write(f"buy,{sum(buy)}\n")
        rep_file.write(f"result,{sum(supply) - sum(buy)}\n")
