def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        lines = data_file.readlines()
    res = {}
    lines = [[line.rstrip().split(",")[0],
              line.rstrip().split(",")[1]] for line in lines]
    for line in lines:
        if line[0] not in res:
            res[line[0]] = int(line[1])
        else:
            res[line[0]] += int(line[1])
    res["result"] = res["supply"] - res["buy"]
    report = "supply,{}\nbuy,{}\nresult,{}\n".format(res["supply"],
                                                     res["buy"], res["result"])
    with open(report_file_name, "w") as report_file:
        report_file.write(report)
