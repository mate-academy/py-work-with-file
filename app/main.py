import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_ls = []
    buy_ls = []
    with open(data_file_name, "r") as f:
        read_f = csv.reader(f)
        for i in read_f:
            if i[0] == "supply":
                supply_ls.append(int(i[1]))
            elif i[0] == "buy":
                buy_ls.append(int(i[1]))
    new_results_ls = [f"supply,{sum(supply_ls)}",
                      f"buy,{sum(buy_ls)}",
                      f"result,{sum(supply_ls) - sum(buy_ls)}"]
    with open(report_file_name, "w") as f:

        for i in new_results_ls:
            f.write(str(i) + "\n")
