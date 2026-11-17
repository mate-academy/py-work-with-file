def create_report(data_file_name: str, report_file_name: str) -> None:

    dt = {"supply": 0, "buy": 0}

    with (open(data_file_name) as file):
        for ln in file.readlines():
            if "," in ln:
                dt[ln.strip().split(",")[0]] += int(ln.strip().split(",")[1])

    with open(report_file_name, "w") as report:
        report.write(
            f"supply,{dt['supply']}\n"
            f"buy,{dt['buy']}\n"
            f"result,{dt['supply'] - dt['buy']}\n"
        )
