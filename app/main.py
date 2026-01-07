# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    file_r = open(data_file_name, "r")
    file_w = open(report_file_name, "w",encoding="utf-8")

    dictt = {}
    for line in file_r.readlines():
        name, price = line.split(",")
        if name not in dictt:
            dictt[name] = int(price)
        else:
            dictt[name] += int(price)
    file_r.close()

    dictt["result"] = dictt["supply"] - dictt["buy"]

    file_w.write(f"supply,{dictt.get('supply')}\n")
    file_w.write(f"buy,{dictt.get('buy')}\n")
    file_w.write(f"result,{dictt.get('result')}\n")
    file_w.close()
