def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as f:
        answer = {"buy" : 0,
                  "supply" : 0}
        result = []
        lines = f.read()
        listoflines = lines.split("\n")
        for i in listoflines:
            if i == "":
                continue
            result.append(i.split(","))
        supply = [int(i[1]) for i in result if i[0][0] == "s"]
        buy = [int(i[1]) for i in result if i[0][0] == "b"]
        answer["supply"] = sum(supply)
        answer["buy"] = sum(buy)
        with open(report_file_name, "a") as fil:
            fil.write(f"supply,{answer['supply']}\n")
            fil.write(f"buy,{answer['buy']}\n")
            fil.write(f"result,{answer['supply']-answer['buy']}\n")
