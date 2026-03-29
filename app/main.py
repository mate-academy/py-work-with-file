#
def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data,
          open(report_file_name, "w") as report):
        answer = {}
        temp = data.read().splitlines()
        for i in temp:
            i = i.split(",")
            if answer.get(i[0]):
                answer[i[0]] += int(i[1])
            else:
                answer[i[0]] = int(i[1])
        answer["result"] = answer["supply"] - answer["buy"]
        report.write(f"supply,{answer['supply']}\n")
        report.write(f"buy,{answer['buy']}\n")
        report.write(f"result,{answer['result']}\n")
