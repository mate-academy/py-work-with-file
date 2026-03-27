def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as file:
        goods = {"supply": 0, "buy": 0, "result": 0}
        for line in file:
            name, amount = line.split(",")
            goods[name] += int(amount)
        goods["result"] = goods["supply"] - goods["buy"]

    with open(report_file_name, "w") as f:
        for key, value in goods.items():
            f.write(key + "," + str(value) + "\n")
