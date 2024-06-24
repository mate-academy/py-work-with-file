def create_report(data_file_name: str, report_file_name: str) -> None:
    file_open = open(f"../{data_file_name}")
    table = file_open.read()
    table = table.split("\n")
    supply = 0
    buy = 0
    for element in table:
        split_element = element.split(",")
        if split_element == [""]:
            break
        if split_element[0] == "supply":
            supply += int(split_element[1])
        else:
            buy += int(split_element[1])
    result = supply - buy
    file_open.close()
    file_open = open(f"{report_file_name}", "w")
    file_open.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
    file_open.close()
