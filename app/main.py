def create_report(data_file_name: str,
                  report_file_name: str
                  ) -> None:
    new_file = open(report_file_name,"w")
    check_file = open(data_file_name)
    values = {}
    for line in check_file.readlines():
        use_one = line.strip().split(",")
        key = use_one[0].strip()
        if key in values:
            values[key] += int(use_one[1])
        else:
            values[key] = int(use_one[1])
    check_file.close()
    values["result"] = values["supply"] - values["buy"]
    for name in ("supply", "buy", "result"):
        new_file.write(f"{name},{values[name]}\n")
    new_file.close()
