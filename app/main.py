def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as f:
        supply = 0
        buy = 0
        for line in f:
            arr = line.split(",")
            if arr[0] == "supply":
                supply += int(arr[1])
            elif arr[0] == "buy":
                buy += int(arr[1])

    with open(report_file_name, "a") as res:
        res.write(f"supply,{supply}\n")
        res.write(f"buy,{buy}\n")
        res.write(f"result,{supply - buy}\n")


create_report("apples.csv", "result_test.csv")
