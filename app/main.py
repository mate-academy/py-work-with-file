def create_report(data_file_name: str, report_file_name: str) -> None:
    res = {"supply": 0, "buy": 0, "result": 0}
    with (open(data_file_name, "r") as r_file,
          open(report_file_name, "w") as w_file):
        for line in r_file.readlines():
            ll = line.split(",")
            if ll[0] == "supply":
                res["supply"] += int(ll[1])
            else:
                res["buy"] += int(ll[1])
        res["result"] = res["supply"] - res["buy"]
        for key, value in res.items():
            w_file.write(str(key) + "," + str(value) + "\n")
