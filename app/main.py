def create_report(data_file_name: str, report_file_name: str) -> None:
    file_to_read = open(data_file_name, "r")
    results = {"supply": 0, "buy": 0, "result": 0}

    for line in file_to_read:
        curr_line = line.strip()
        if not curr_line:
            continue

        current = curr_line.split(",")
        results[current[0]] += int(current[1])

    file_to_read.close()
    results["result"] = results["supply"] - results["buy"]

    report = [
        f"supply,{results['supply']}\n",
        f"buy,{results['buy']}\n",
        f"result,{results['result']}\n",
    ]

    file_to_write = open(report_file_name, "w")
    file_to_write.writelines(report)
    file_to_write.close()
