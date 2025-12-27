def create_report(data_file_name: str, report_file_name: str) -> None:
    project_file = open(data_file_name, "r")
    results = {"supply": 0, "buy": 0, "result": 0}
    for line in project_file.readlines():
        line = line.split(",")
        results[line[0]] += int(line[1])
    results["result"] = results["supply"] - results["buy"]
    project_file.close()
    with open(report_file_name, "w") as file:
        for key, value in results.items():
            file.write("{},{}\n".format(key, value))
