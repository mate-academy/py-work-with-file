# write your code here


def create_report(data_file_name: str, report_file_name: str) -> str:
    supply = 0
    buy = 0
    result = 0
    with open(data_file_name) as file:
        stroki = file.readlines()
        for s in stroki:
            s = s.strip()
            s = s.split(",")
            a = int(s[1])
            if s[0] == "supply":
                supply += a
            elif s[0] == "buy":
                buy += a
    result = supply - buy

    with open(report_file_name, "wt") as e:
        e.write(f"supply,{supply}\n")
        e.write(f"buy,{buy}\n")
        e.write(f"result,{result}\n")
