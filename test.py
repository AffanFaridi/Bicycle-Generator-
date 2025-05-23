import unittest
import pandas as pd
import tempfile
import os
import json
from bicycle import bikes  # Make sure your function is in bicycle.py

class TestBikesFunction(unittest.TestCase):
    def setUp(self):
        # Prepare minimal Excel data for all sheets
        self.data = {
            'ID': pd.DataFrame({
                'Model number': ['M1'],
                'Brakes': ['B1'],
                'Wheels': ['W1'],
                'Frame size': ['F1'],
                'Groupset': ['G1'],
                'Suspension': ['S1'],
                'Color': ['C1']
            }),
            'GENERAL': pd.DataFrame([{'Manufacturer': 'Bikes INC', 'Type': 'City', 'Logo': '1'}]),
            '1': pd.DataFrame([{'Brakes': 'B1', 'Brake Type': 'Disc'}]),
            '2': pd.DataFrame([{'Wheels': 'W1', 'Wheel Size': '29'}]),
            '3': pd.DataFrame([{'Frame size': 'F1', 'Frame type': 'Diamond', 'Frame material': 'Aluminum'}]),
            '4': pd.DataFrame([{'Groupset': 'G1', 'Speed': '21'}]),
            '5': pd.DataFrame([{'Suspension': 'S1', 'Has suspension': '1'}]),
            '6': pd.DataFrame([{'Color': 'C1', 'Color Name': 'Red'}])
        }

        # Create a temp Excel file
        self.temp_dir = tempfile.TemporaryDirectory()
        self.excel_path = os.path.join(self.temp_dir.name, "test_bicycle.xlsx")
        with pd.ExcelWriter(self.excel_path) as writer:
            for sheet, df in self.data.items():
                df.to_excel(writer, sheet_name=sheet, index=False)

    def tearDown(self):
        # Cleanup: remove output.json and temp dir
        if os.path.exists("output.json"):
            os.remove("output.json")
        self.temp_dir.cleanup()

    def test_bikes_output(self):
        # Run the bikes function (should write output.json)
        bikes(self.excel_path)

        # Load the output
        with open("output.json", "r") as f:
            output = json.load(f)

        # Check: output is a non-empty list
        self.assertIsInstance(output, list)
        self.assertTrue(len(output) > 0)

        # Check: the first (and only) bike has expected fields and values
        bike = output[0]
        self.assertEqual(bike['ID'], 'M1B1W1F1G1S1C1')
        self.assertEqual(bike['Manufacturer'], 'Bikes INC')
        self.assertEqual(bike['Type'], 'City')
        self.assertEqual(bike['Logo'], 'TRUE')
        self.assertEqual(bike['Brake Type'], 'Disc')
        self.assertEqual(bike['Wheel Size'], '29')
        self.assertEqual(bike['Frame type'], 'Diamond')
        self.assertEqual(bike['Frame material'], 'Aluminum')
        self.assertEqual(bike['Speed'], '21')
        self.assertEqual(bike['Has suspension'], 'TRUE')
        self.assertEqual(bike['Color Name'], 'Red')

if __name__ == "__main__":
    unittest.main()
