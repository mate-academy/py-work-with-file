def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as f_read:
        supply = []
        buy = []
        for i in f_read.readlines():
            if i.startswith("s"):
                supply.append(i.replace("\n", ""))
            if i.startswith("b"):
                buy.append(i.replace("\n", ""))
    num_s = []
    num_b = []
    for elem in supply:
        num_s.append(int(elem.split(",")[1]))
    for elem in buy:
        num_b.append(int(elem.split(",")[1]))
    with open(report_file_name, "a") as f:
        f.write(f"supply,{sum(num_s)}\n")
        f.write(f"buy,{sum(num_b)}\n")
        f.write(f"result,{sum(num_s) - sum(num_b)}\n")
