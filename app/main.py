def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(data_file_name, "r") as inp, open(report_file_name, "w") as out:
        dt = {"supply": 0, "buy": 0}
        for name, data in [line.split(",") for line in inp]:
            dt[name] += int(data)

        dt["result"] = dt["supply"] - dt["buy"]

        for name, data in dt.items():
            print(name + "," + str(data), file=out)
