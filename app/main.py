def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as f:
        line = f.readline()
        report = {"supply": 0, "buy": 0, "result": 0}
        while line != "":
            if "supply" in line:
                report["supply"] += int(line.split(",")[1])
                report["result"] += int(line.split(",")[1])
            if "buy" in line:
                report["buy"] += int(line.split(",")[1])
                report["result"] -= int(line.split(",")[1])
            line = f.readline()
        with open(report_file_name, "w") as r:
            r.write(f"supply,{report['supply']}\n"
                    f"buy,{report['buy']}\n"
                    f"result,{report['result']}\n")
