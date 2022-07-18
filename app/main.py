def create_report(data_file_name: str, report_file_name: str):
    data_file_name = f'C:/Users/Bodnarchuk/Desktop/Project/' \
                     f'study-project/py-work-with-file/{data_file_name}'
    with open(data_file_name, "r") as data_r:
        lines = data_r.readlines()
        s, b = 0, 0
        for line in lines:
            line = line.split(",")
            if "supply" in line:
                s += int(line[1])
            if "buy" in line:
                b += int(line[1])
        sup = f"supply,{s}"
        buy = f"buy,{b}"
        result = f"result,{s - b}"
        res = [sup, buy, result]
        res = "\n".join(res) + "\n"
        with open(report_file_name, "w") as rep_w:
            rep_w.write(res)
