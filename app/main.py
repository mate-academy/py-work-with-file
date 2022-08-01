def create_report(data_file_name: str, report_file_name: str):
    sup = 0
    buy_l = 0
    with open(data_file_name, 'r') as f, open(report_file_name, 'w') as f2:
        rep = f.readlines()
        for row in rep:
            line = row.split(",")
            if line[0] == 'supply':
                sup += int(line[1])
            else:
                buy_l += int(line[1])
        f2.write("supply," + str(sup) + "\n" + "buy," + str(
            buy_l) + "\nresult," + str(sup - buy_l) + "\n")
