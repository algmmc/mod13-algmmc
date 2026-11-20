"""Unit tests for the five Project 3 stock visualizer inputs."""

import unittest
from datetime import date

from user_input import (
    CHART_TYPES,
    TIME_SERIES,
    validate_date,
    validate_menu_choice,
    validate_symbol,
)


class TestStockVisualizerInputs(unittest.TestCase):
    def test_symbol(self):
        for value, expected in (
            ("A", "A"),
            ("aapl", "AAPL"),
            ("ABCDEFG", "ABCDEFG"),
        ):
            with self.subTest(value=value):
                self.assertEqual(validate_symbol(value), expected)

        for value in ("", "AA1", "AA-B", "ABCDEFGH"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    validate_symbol(value)

    def test_chart_type(self):
        self.assertEqual(validate_menu_choice("1", CHART_TYPES), "bar")
        self.assertEqual(validate_menu_choice("2", CHART_TYPES), "line")
        for value in ("", "0", "3", "12", "a"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    validate_menu_choice(value, CHART_TYPES)

    def test_time_series(self):
        for value, expected in (
            ("1", "TIME_SERIES_INTRADAY"),
            ("2", "TIME_SERIES_DAILY"),
            ("3", "TIME_SERIES_WEEKLY"),
            ("4", "TIME_SERIES_MONTHLY"),
        ):
            with self.subTest(value=value):
                self.assertEqual(validate_menu_choice(value, TIME_SERIES), expected)

        for value in ("", "0", "5", "11", "a"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    validate_menu_choice(value, TIME_SERIES)

    def test_start_date(self):
        self.assertEqual(validate_date("2024-02-29"), date(2024, 2, 29))
        for value in ("", "02/29/2024", "2024-2-29", "2025-02-29"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    validate_date(value)

    def test_end_date(self):
        self.assertEqual(validate_date("2026-11-30"), date(2026, 11, 30))
        for value in ("", "11/30/2026", "2026-11-9", "2026-11-31"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    validate_date(value)


if __name__ == "__main__":
    unittest.main()
