

def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {}
    file_in = open(data_file_name, "r")
    for line in file_in.readlines():
        line = line.strip()
        if not line:
            continue
        op, amt_str = line.split(",", 1)
        op = op.strip()
        amt = int(amt_str.strip())
        if op not in report_dict:
            report_dict[op] = amt
        else:
            report_dict[op] += amt
        supply = report_dict.get("supply",0)
        buy = report_dict.get("buy",0)
        result = supply - buy
        with open(report_file_name, "w", encoding="utf-8") as outfile:
            outfile.write(f"supply,{supply}\n")
            outfile.write(f"buy,{buy}\n")
            outfile.write(f"result,{result}\n")
