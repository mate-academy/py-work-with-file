def create_report(
        data_file_name: str,
        report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as file_in,
        open(report_file_name, "w") as file_out
    ):
        file_in_copy = file_in.read().replace("\n", ",").split(",")
        file_in.close()
        action = None
        info = {"supply": 0, "buy": 0, "result": 0}

        for string in file_in_copy:
            if action is None:
                action = string
                continue
            info[action] += int(string)
            action = None

        info["result"] += info["supply"] - info["buy"]
        info1 = f"supply,{info['supply']}\nbuy,"
        info2 = f"{info['buy']}\nresult,{info['result']}"

        file_out.write(info1 + info2)
        file_out.close()
