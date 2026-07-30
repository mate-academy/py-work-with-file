def create_report(
        data_file_name: str, report_file_name: str
) -> None:
    text = open(data_file_name, "r")
    arr = [char.strip().split(",") for char in text]
    result = {}
    for num in arr:
        if num[0] in result:
            result[num[0]] += int(num[1])
        else:
            result[num[0]] = int(num[1])
    result["result"] = result["supply"] - result["buy"]

    print(result)
    with open(report_file_name, "w") as f:
        f.write(f"supply,{result['supply']}\n")
        f.write(f"buy,{result['buy']}\n")
        f.write(f"result,{result['result']}\n")
