def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    temp = {"supply": 0, "buy": 0, "result": 0}
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        for line in data_file.read().splitlines():
            if line.split(",")[0] == "supply":
                temp["supply"] += int(line.split(",")[1])
            if line.split(",")[0] == "buy":
                temp["buy"] += int(line.split(",")[1])
        temp["result"] = temp["supply"] - temp["buy"]
        for key, value in temp.items():
            report_file.write(f"{key},{str(value)}\n")
        report_file.write("")
