def create_report(data_file_name: str, report_file_name: str) -> None:
    res = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as csv_file:
        for row in csv_file.readlines():
            row = row.split(",")
            res[row[0]] += int(row[1])

    res["result"] = res["supply"] - res["buy"]
    res = "".join([f"{name},{amount}\n" for name, amount in res.items()])

    with open(report_file_name, "w") as csv_file:
        csv_file.write(res)
