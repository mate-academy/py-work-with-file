def create_report(data_file_name: str, report_file_name: str) -> None:
    sum1 = 0
    sum2 = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            aaa = line.strip()
            if not aaa:
                continue
            aa, bbb = aaa.split(",")
            bb = int(bbb)
            if aa == "supply":
                sum1 += bb
            elif aa == "buy":
                sum2 += bb
        sum3 = sum1 - sum2
        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{sum1}"
                              f"\n"f"buy,{sum2}\n"f"result,{sum3}\n")
