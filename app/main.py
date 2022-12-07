def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f, open(report_file_name, "w") as q:
        supply_sum, buy_sum = 0, 0
        while True:
            a = f.readline().split(",")
            if a[0] == "supply":
                supply_sum += int(a[1])
            elif a[0] == "buy":
                buy_sum += int(a[1])
            else:
                break
        q.write(f"supply,{supply_sum}\n"
                f"buy,{buy_sum}\n"
                f"result,{supply_sum - buy_sum}\n"
                )
