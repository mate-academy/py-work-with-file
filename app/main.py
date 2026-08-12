def create_report(data_file_name: str, report_file_name: str) -> None:
    dic = {}
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        for i in data_file:
            text = i.split(",")
            if text[0] not in dic:
                dic[text[0]] = int(text[1])
            else:
                print(dic[text[0]], text[1])
                dic[text[0]] = dic[text[0]] + int(text[1])
        dic["result"] = dic["supply"] - dic["buy"]
        report_file.write(f"supply,{dic['supply']}\n")
        report_file.write(f"buy,{dic['buy']}\n")
        report_file.write(f"result,{dic['result']}\n")
