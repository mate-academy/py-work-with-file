def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_info:
        temp = file_info.read()
    temp = temp.split("\n")
    calculate = dict(buy=0, supply=0)
    for elementh in temp:
        elmnt = elementh.split(",")
        if len(elmnt) == 2:
            calculate[elmnt[0]] = calculate.get(elmnt[0]) + int(elmnt[1])
    out = f"supply,{calculate['supply']}\nbuy,{calculate['buy']}\n" \
          f"result,{calculate['supply'] - calculate['buy']}\n"
    with open(report_file_name, "w") as file_report:
        file_report.write(out)
