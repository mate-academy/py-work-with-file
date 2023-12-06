def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file, open(report_file_name, "w") as result_file:
        suply, buy, = [], []
        for string in file:
            arg = string.split(",")
            if arg[0] == "suply":
                suply.append(arg[1])
            elif arg[0] == "buy":
                buy.append(arg[1])
        result_file.write(f"supply = {' + '.join(suply)} = {sum(suply)}")
        result_file.write(f"supply = {' + '.join(buy)} = {sum(buy)}")
        result_file.write(f"result = supply - buy = {sum(suply)} - {sum(buy)} = {sum(suply) - sum(buy)}")
