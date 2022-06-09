def create_report(data_file_name: str, report_file_name: str):

    with open(data_file_name, "r") as fin, open(report_file_name, "w") as fout:
        buy = 0
        supply = 0

        lines = fin.readlines()
        for line in lines:
            for i in range(len(line) - 1):
                if line[i] == ',':
                    number = line[i + 1: len(line) - 1]
                    if line[0] == 'b':
                        buy += int(number)
                    if line[0] == 's':
                        supply += int(number)

        res = supply - buy
        print(f"Supply: {supply}")
        print(f"Buy: {buy}")
        print(f"Res: {res}")

        fout.writelines(f"supply,{supply}\nbuy,{buy}\nresult,{res}\n")
