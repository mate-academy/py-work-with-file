def create_report(
        data_file_name: str, report_file_name: str
) -> None:
    with open(data_file_name, "r") as file_in, \
            open(report_file_name, "w") as file_out:
        result = {"supply": 0, "buy": 0}
        lst = file_in.read().replace("\n", ",").split(",")
        for i in range(0, len(lst) - 1, 2):
            result[lst[i]] = result.get(lst[i], 0) + int(lst[i + 1])
        result["result"] = result["supply"] - result["buy"]
        for key in result:
            # bypassing E231 missing whitespace after ','
            line = f"{key}!{result[key]}\n"
            line = line.replace("!", ",")
            file_out.write(line)
