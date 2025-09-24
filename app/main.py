import csv
from collections import OrderedDict


def create_report(data_file_name: str, report_file_name: str) -> None:
    dict_ls = OrderedDict()
    with open(data_file_name, encoding="utf-8") as file_csv:
        csv_dict = csv.reader(file_csv, delimiter=",")
        for i in csv_dict:
            key = i[0]
            value = int(i[1])
            if key not in dict_ls:
                dict_ls[key] = value
            else:
                dict_ls[key] += value
    dict_ls["result"] = dict_ls["supply"] - dict_ls["buy"]

    key_order = ["supply", "buy", "result"]
    with open(report_file_name, "w", newline="") as rep_file:
        writer_ls = csv.writer(rep_file, delimiter=",")
        for key in key_order:
            if key in dict_ls:
                writer_ls.writerow([key, dict_ls[key]])
