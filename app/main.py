def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(data_file_name, "r") as f:
        supply = 0
        buy = 0
        for line in f.read().split("\n"):
            arr = line.split(",")
            if arr[0] == "supply":
                supply += int(arr[1])
            elif arr[0] == "buy":
                buy += int(arr[1])
        with open(report_file_name, "w") as f_w:
            f_w.write(f"supply,{supply}\n"
                      f"buy,{buy}\n"
                      f"result,{supply - buy}\n")


create_report("apples.csv", "report.csv")
