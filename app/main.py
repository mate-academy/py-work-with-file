def create_report(data_file_name: str, report_file_name: str) -> None:
    try:
        inp = open("../" + data_file_name, "r")
        sum_list = {"supply": 0, "buy": 0}
        for line in inp:
            data = line.split(",")
            sum_list[data[0]] += int(data[1])
        inp.close()
        out = open(report_file_name, "w")
        for line in sum_list:
            out.write(f"{line},{sum_list[line]}\n")
        out.write(f"result,{sum_list["supply"] - sum_list["buy"]}\n")
        out.close()
    except FileNotFoundError:
        print("File is not found!")
