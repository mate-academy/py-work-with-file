def create_report(data_file_name: str, report_file_name: str) -> None:
    with open("..//" + data_file_name, "r") as first, open(report_file_name,
                                                           "a") as second:
        data1 = []
        for line in first:
            line = line[0:-1]
            data1.append(line.split(","))
        print(data1)

        supply = 0
        buy = 0

        for el in data1:
            if el[0] == "supply":
                supply += int(el[1])
            else:
                buy += int(el[1])
        result = supply - buy

        second.write(f"supply,{supply}\n")
        second.write(f"buy,{buy}\n")
        second.write(f"result,{result}\n")
