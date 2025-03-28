def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f:
        supply = 0
        buy = 0
        for line in f:
            lst = line.split(",")
            if lst[0] == "buy":
                buy += int(lst[1])
            else:
                supply += int(lst[1])
    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{supply - buy}\n")
