def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as infile:
        res = {"supply": 0, "buy": 0}
        while True:
            data = infile.readline()
            if data == "":
                break
            reso = data.split(",")
            res[reso[0]] += int(reso[1])
    with open(report_file_name, "w") as outfile:
        outfile.write(f"supply,{res['supply']}\n")
        outfile.write(f"buy,{res['buy']}\n")
        outfile.write(f"result,{res['supply'] - res['buy']}\n")
