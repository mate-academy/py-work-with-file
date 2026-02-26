def create_report(data_file_name: str, report_file_name: str) -> None:
    result_csv = {"supply": 0, "buy": 0, "result": 0}
    with open(data_file_name, "r") as file_csv:
        data_csv = file_csv.read()

        rows = data_csv.split("\n")

        for row in rows:
            if len(row) == 0:
                continue

            columns = row.split(",")
            if columns[0] == "supply":
                result_csv["supply"] += int(columns[1])
            if columns[0] == "buy":
                result_csv["buy"] += int(columns[1])

    result_csv["result"] = result_csv["supply"] - result_csv["buy"]

    with open(report_file_name, "w") as file_output:
        file_output.writelines([
            f"supply,{result_csv['supply']}\n",
            f"buy,{result_csv['buy']}\n",
            f"result,{result_csv['result']}\n",
        ])
