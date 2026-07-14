def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    with open(data_file_name, "r") as file_d:
        sup_result, buy_result = 0, 0
        for line in file_d:
            if "supply" in line:
                parts = line.split(",")
                sup_result += int(parts[1])
            if "buy" in line:
                parts = line.split(",")
                buy_result += int(parts[1])
        result = sup_result - buy_result
        with open(report_file_name, "w") as file_r:
            file_r.write(f"supply,{str(sup_result)}\n")
            file_r.write(f"buy,{str(buy_result)}\n")
            file_r.write(f"result,{str(result)}\n")
