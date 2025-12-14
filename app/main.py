# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    suply = 0
    buy = 0
    main_file = open(data_file_name)
    for line in main_file:
        aux_list = line.split(",")
        qnt = int(aux_list[1].rstrip("\n"))
        if line[0] == "s":
            suply += qnt
        elif line[0] == "b":
            buy += qnt
    result = suply - buy
    main_file.close()

    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{suply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{result}\n")
    report_file.close()
