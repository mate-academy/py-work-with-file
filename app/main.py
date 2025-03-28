def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f_in:
        res = {}
        for line_in in f_in:
            values = line_in.split(",")
            if values[0] not in res:
                res[values[0]] = int(values[1].rstrip("\n"))
            else:
                res[values[0]] += int(values[1].rstrip("\n"))
    with open(report_file_name, "w") as f_out:
        f_out.write(f"supply,{res['supply']}\n")
        f_out.write(f"buy,{res['buy']}\n")
        f_out.write(f"result,{res['supply'] - res['buy']}\n")
