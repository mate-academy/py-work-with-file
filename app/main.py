def create_report(data_file_name: str, report_file_name: str) -> None:
    final_res = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file:
        for line in file.readlines():
            line = line.split(",")
            final_res[line[0]] += int(line[1])

    final_res["result"] = final_res["supply"] - final_res["buy"]
    text = "".join(f"{name},{amount}\n" for name, amount in final_res.items())

    with open(report_file_name, "w") as rep_file:
        rep_file.write(text)
