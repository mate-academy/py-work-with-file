def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as fn:
        lines = fn.readlines()
    res = {"supply": 0, "buy": 0}
    for i in lines:
        i = i.strip().split(",")
        if len(i) == 2:  # To handle any empty lines gracefully
            res[i[0]] += int(i[1])
    rir = (
        f"supply,{res['supply']}\n"
        f"buy,{res['buy']}\n"
        f"result,{res['supply'] - res['buy']}\n"
    )
    with open(report_file_name, "w") as fn:
        fn.write(rir)
