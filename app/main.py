def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as file_out,
        open(report_file_name, "a+") as file_in
    ):
        content = {}
        for line in file_out.read().split("\n"):
            if len(line) != 0 and line.split(",")[0] in content:
                content[line.split(",")[0]] += int(line.split(",")[1])
            elif len(line) != 0 and line.split(",")[0] not in content:
                content[line.split(",")[0]] = int(line.split(",")[1])
        content["result"] = content["supply"] - content["buy"]

        file_in.write(
            f"supply,{content['supply']}\n"
            f"buy,{content['buy']}\n"
            f"result,{content['result']}\n"
        )
