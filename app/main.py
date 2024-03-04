def create_report(data_file_name: str, report_file_name: str):
    sorted_data = {"supply": 0, "buy": 0, "result": 0}
    with open(data_file_name, "r") as incoming_data:
        i = 0
        while True:
            line = incoming_data.readline().split(",")
            if len(line) == 1:
                break
            operation = line[0]
            j = 0
            for i in range(len(line[1])):
                if line[1][i].isnumeric():
                    j += 1
            amount = int(line[1][:j])
            sorted_data[operation] += amount
    with open(report_file_name, "w") as f:
        f.write(f'supply,{sorted_data["supply"]}\n')
        f.write(f'buy,{sorted_data["buy"]}\n')
        f.write(f'result,{sorted_data["supply"] - sorted_data["buy"]}\n')
