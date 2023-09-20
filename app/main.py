def create_report(data_file_name: str, report_file_name: str) -> None:
    res = {
        "supply": 0,
        "buy": 0
    }
    with open(data_file_name, "r") as data_file:
        with open(report_file_name, "w") as report_file:
            for line in data_file.readlines():
                line_ls = line.split(",")
                res.update({line_ls[0]: int(line_ls[1]) + res[line_ls[0]]})
            report_file.write(
                f"supply,{res['supply']}\n"
                f"buy,{res['buy']}\n"
                f"result,{res['supply'] - res['buy']}\n"
            )
