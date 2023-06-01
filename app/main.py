# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:

    if data_file_name == report_file_name:
        raise ValueError("Files must have another names")
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "a") as report):
        buy, supply = 0, 0
        for line in file_in:
            res_lst = line.replace("\n", "").split(",")
            if res_lst[0] == "supply":
                supply += int(res_lst[1])
            else:
                buy += int(res_lst[1])
        result = supply - buy
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
