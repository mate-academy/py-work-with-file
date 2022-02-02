def create_report(data_file_name: str, report_file_name: str):
    newls = []
    with open(data_file_name) as f:
        ls = f.readlines()
    if len(ls[-1]) == 0:
        ls.pop(-1)
    for i in ls:
        newls.append(i.split(","))
    supply = 0
    buy = 0
    for m in range(len(newls)):
        if newls[m][0] == "supply":
            supply += int(newls[m][1])
        if newls[m][0] == "buy":
            buy += int(newls[m][1])
    result = supply - buy
    with open(report_file_name, "a") as f1:
        f1.writelines(f"supply,{supply}\n")
        f1.writelines(f"buy,{buy}\n")
        f1.writelines(f"result,{result}\n")
