# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    from_file = open(data_file_name)
    to_file = open(report_file_name, "w")

    result = {
        "supply": 0,
        "buy": 0,
        "result": 0,
    }

    for line in from_file.readlines():
        if len(line) > 0:
            text = line.split(",")
            result[text[0]] += int(text[1])
    from_file.close()

    result["result"] = result["supply"] - result["buy"]

    for key, item in result.items():
        to_file.write(f"{key},{item}\n")
    to_file.close()
