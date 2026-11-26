def create_report(data_file_name: str, report_file_name: str) -> None:
    dict1 = {}
    with open(data_file_name, "r") as f:
        for line in f:
            if line.strip():
                list1 = line.split(",")
                if list1[0] in dict1:
                    dict1[list1[0]] += int(list1[1])
                else:
                    dict1[list1[0]] = int(list1[1])
    with open(report_file_name, "w") as f:
        result = dict1.get("supply", 0) - dict1.get("buy", 0)
        f.write(f'supply,{dict1["supply"]}\n')
        f.write(f'buy,{dict1["buy"]}\n')
        f.write(f"result,{result}\n")
