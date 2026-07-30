def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    print("read: ",data_file_name)
    print("write: ",report_file_name)
    read_file = open(data_file_name)
    totals = dict()
    for line in read_file:
        split = line.split(",")
        if split[0] not in totals:
            totals[split[0]] = 0
        totals[split[0]] += int(split[1])
    supply = totals["supply"]
    buy = totals["buy"]
    result = supply - buy
    read_file.close()
    write_file = open(report_file_name,"w")
    write_file.write(f"supply,{supply}\n")
    write_file.write(f"buy,{buy}\n")
    write_file.write(f"result,{result}\n")
    write_file.close()
