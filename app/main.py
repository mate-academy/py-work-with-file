def create_report(data_file_name: str, report_file_name: str):
    arr1 = []
    dict1 = {
        "supply": 0,
        "buy": 0
    }

    with open(data_file_name, "r") as f:
        for line in f.readlines():
            if line:
                arr1.append(line.replace("\n", "").split(","))
        for i in arr1:
            dict1[i[0]] += int(i[1])

        dict1["result"] = dict1["supply"] - dict1["buy"]

        with open(report_file_name, "w") as f2:
            f2.write(f"supply,{dict1['supply']}\n"
                     f"buy,{dict1['buy']}\n"
                     f"result,{dict1['result']}\n"
                     )
