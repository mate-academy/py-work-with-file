def create_report(data_file_name: str, report_file_name: str) -> None:
    file = open(data_file_name, "r")
    report_file = open(report_file_name, "w+")

    arr = []
    result = {}

    for line in file:
        key = line.split(",")[0]
        value = int(line.split(",")[1].replace("\n", ""))
        arr.append([key, value])

    for el_arr in arr:
        el_key = el_arr[0]
        el_value = el_arr[1]

        if el_key in result:
            result[el_key] += el_value
        else:
            result[el_key] = el_value

    result['result'] = result.get('supply', 0) - result.get('buy', 0)
    report_file.write(f"supply,{result['supply']}\n")
    report_file.write(f"buy,{result['buy']}\n")
    report_file.write(f"result,{result['result']}\n")

    file.close()
    report_file.close()
