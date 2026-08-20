from __future__ import annotations

from app.main import create_report
from tests.test_main import CleanUpFile


def test_create_report_skips_malformed_rows() -> None:
    create_report("malformed.csv", "malformed_report.csv")

    with CleanUpFile("malformed_report.csv"):
        with open("malformed_report.csv", "r") as report_file:
            assert report_file.read() == "supply,30\nbuy,10\nresult,20\n"


def test_create_report_ignores_unknown_operation_type() -> None:
    create_report("unknown_operation.csv", "unknown_operation_report.csv")

    with CleanUpFile("unknown_operation_report.csv"):
        with open("unknown_operation_report.csv", "r") as report_file:
            assert report_file.read() == "supply,30\nbuy,10\nresult,20\n"
