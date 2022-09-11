import csv


def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, 'r') as infile:
        reader = csv.reader(infile)
        with open(report_file_name, 'w') as outfile:
            writer = csv.writer(outfile)
            num_dict = {}
            for t in reader:
                if t[0] in num_dict:
                    num_dict[t[0]] = int(num_dict[t[0]]) + int(t[1])
                else:
                    num_dict[t[0]] = int(t[1])
            res = int(num_dict["supply"]) - int(num_dict["buy"])
            num_dict.update({"result": res})
            for key, value in sorted(num_dict.items(),
                                     key=lambda pair: pair[1],
                                     reverse=True):
                writer.writerow([key, value])
