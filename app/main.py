def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:

    with open(data_file_name, "r") as file:
        res = {
            "supply": 0,
            "buy": 0
        }
        for line in file:
            if line.strip() == "":
                continue
            splitted = line.split(",")
            if splitted[0] in res:
                res[splitted[0]] += int(splitted[1].strip())
        result = res["supply"] - res["buy"]

    with open(report_file_name, "w") as file:
        file.write(f"supply,{res['supply']}\n")
        file.write(f"buy,{res['buy']}\n")
        file.write(f"result,{result}\n")
