import os


def create_report(data_file_name: str, report_file_name: str) -> None:
    cur_path = os.getcwd()
    new_path = cur_path[:cur_path.rfind("\\")]
    supply = 0
    buy = 0
    with open(new_path + "\\" + data_file_name, "r") as file_in, \
         open(report_file_name, "w") as file_report:
        for line in file_in:
            line_ls = line.split(",")
            if line_ls[0] == "supply":
                supply += int(line_ls[1])
            else:
                buy += int(line_ls[1])

        file_report.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{supply - buy}\n")
