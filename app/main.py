# write your code here


def create_report(data_file_name: str, report_file_name: str) -> str:
    supply = 0
    buy = 0
    result = 0
    with open(data_file_name) as file:
        stroki = file.readlines()
        for st in stroki:
            st = st.strip()
            st = st.split(",")
            num = int(st[1])
            if st[0] == "supply":
                supply += num
            elif st[0] == "buy":
                buy += num
    result = supply - buy

    with open(report_file_name, "wt") as text:
        text.write(f"supply,{supply}\n")
        text.write(f"buy,{buy}\n")
        text.write(f"result,{result}\n")
