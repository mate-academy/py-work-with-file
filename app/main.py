def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as f:
        data_dict = {
            "supply": 0,
            "buy": 0,
            "result": 0
        }
        for line in f:
            if line:
                line_ls = line.split(",")
                data_dict[line_ls[0]] += int(line_ls[1])

        data_dict["result"] = data_dict["supply"] - data_dict["buy"]

        with open(report_file_name, "w") as f2:
            for operation, amount in data_dict.items():
                f2.write(f"{operation},{str(amount)}\n")
