def create_report(data_file_name, report_file_name):
    with open(data_file_name, "r") as initial_data,\
            open(report_file_name, "w") as report_file:
        content = initial_data.read()
        result_dict = {}
        for line in content.strip().split("\n"):
            operation = line.split(",")
            if operation[0] in result_dict:
                result_dict[operation[0]] += int(operation[1])
            else:
                result_dict[operation[0]] = int(operation[1])
        result_dict["result"] = result_dict["supply"] - result_dict["buy"]
        supply = result_dict["supply"]
        buy = result_dict["buy"]
        result = result_dict["result"]
        result_string = f'supply,{supply}\nbuy,{buy}\nresult,{result}\n'
        report_file.write(result_string)
