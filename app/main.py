def create_report(data_file_name: str, report_file_name: str) -> None:

    supply1 = 0
    buy1 = 0
    with open(data_file_name, "r") as file1:
        for row in file1:
            row = row.strip().split(",")
            if row[0] == "supply":
                supply1 += int(row[1])
            if row[0] == "buy":
                buy1 += int(row[1])

    with open(report_file_name, "w") as file2:
        file2.writelines([f"supply,{supply1}\n",
                          f"buy,{buy1}\n",
                          f"result,{supply1 - buy1}\n"])
