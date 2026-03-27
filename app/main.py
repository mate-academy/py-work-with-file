import csv


def create_report(data_file_name: str, report_file_name: str):
    with open(f"{data_file_name}", "r") as f_in,\
            open(f"{report_file_name}", "w") as f_out:

        read_data_new = csv.reader(f_in, delimiter=',')

        supply = 0
        buy = 0

        for row in read_data_new:
            if row[0] == "supply":
                supply += int(row[1])
            if row[0] == "buy":
                buy += int(row[1])

        f_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
