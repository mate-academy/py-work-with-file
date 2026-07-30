def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum = 0
    buy_sum = 0

    with open(data_file_name, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            key, value = line.split(",")
            value = int(value)

            if key == "supply":
                supply_sum += value
            elif key == "buy":
                buy_sum += value

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply_sum}\n"
                f"buy,{buy_sum}\n"
                f"result,{supply_sum - buy_sum}\n")
