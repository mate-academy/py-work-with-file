def create_report(data_file_name: str, report_file_name: str) -> None:
    res = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file_in:
        for line in file_in.readlines():
            new_line = line.strip().split(",")
            key, value = new_line[0], int(new_line[1])
            res[key] += value

    with open(report_file_name, "w") as file_out:
        for key, value in res.items():
            file_out.write(f"{key},{value}\n")
        result = res["supply"] - res["buy"]
        file_out.write(f"result,{result}\n")
