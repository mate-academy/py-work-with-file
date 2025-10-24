def create_report(data_file_name: str, report_file: str) :
    file = open(data_file_name, 'r')
    d = {}
    for line in file :
        d[line.split(",")[0]] += d.get(line.split(",")[0], 0)
    file.close()
    file = open(report_file, 'w')
    for key, value in d.items() :
        file.write(key + "," + str(value) + "\n")


