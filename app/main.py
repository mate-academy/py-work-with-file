def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data, \
            open(report_file_name, "a+") as report:
        res = {}
        for i in data.read().splitlines():
            i = i.split(",")
            if i[0] not in res.keys():
                res[i[0]] = int(i[1])
            else:
                res[i[0]] += int(i[1])
        res["result"] = res["supply"] - res["buy"]
        report.writelines(f"{'supply'},{res['supply']}\n"
                          f"{'buy'},{res['buy']}\n"
                          f"{'result'},{res['result']}\n")
