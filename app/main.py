def create_report(data_file_name: str, report_file_name: str):
    params = {"supply": 0, "buy": 0, "result": 0}
    with open(data_file_name, "r") as file:
        line = file.readline()
        while "," in line:
            name, value = line.split(",")
            params[name] += int(value)
            line = file.readline()

    with open(report_file_name, "w") as file:
        file.write(f'supply,{params["supply"]}\n'
                   f'buy,{params["buy"]}\n'
                   f'result,{params["supply"] - params["buy"]}\n')
