def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dic = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            val_line = line.split(",")
            operation_type = val_line[0]
            amount = int(val_line[1])
            if operation_type == "supply":
                result_dic["supply"] += amount
            elif operation_type == "buy":
                result_dic["buy"] += amount
    result = result_dic["supply"] - result_dic["buy"]
    with open(report_file_name, "w") as f:
        f.write(f"supply,{result_dic['supply']}\n")
        f.write(f"buy,{result_dic['buy']}\n")
        f.write(f"result,{result}\n")
