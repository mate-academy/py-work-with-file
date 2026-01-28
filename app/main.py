def create_report(data_file_name: str, report_file_name: str) -> None:
    file_read = open(data_file_name, "r")
    file_write = open(report_file_name, "w")
    file_write.write(file_read.read())
    file_read.close()
    file_write.close()
