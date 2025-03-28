def create_report(data_file_name: str, report_file_name: str):
    operations = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            name, cost = line.split(',')
            cost = cost.replace("\n", "")
            operations[name] += int(cost)

    with open(report_file_name, "w") as file:
        file.write(f"supply,{operations['supply']}\n")
        file.write(f"buy,{operations['buy']}\n")
        file.write(f"result,{operations['supply'] - operations['buy']}\n")
