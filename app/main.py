def create_report(data_file_name: str, report_file_name: str) -> None:
    file_source = open(data_file_name, "r")
    file_destination = open(report_file_name, "w")
    supply = 0
    buy = 0
    for line in file_source:
        pairs = line.split(",")
        match pairs[0]:
            case "buy":
                buy += int(pairs[1])
            case "supply":
                supply += int(pairs[1])
    result = supply - buy
    file_destination.write(f"supply,{supply}\n")
    file_destination.write(f"buy,{buy}\n")
    file_destination.write(f"result,{result}\n")
    file_source.close()
    file_destination.close()
