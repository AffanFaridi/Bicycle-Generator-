# Bicycle Generator

## Problem Statement

Managing all possible combinations of bicycle parts and options (like frame, wheels, brakes, color, etc.) is difficult and tedious to do by hand. There is a need for a simple way to automatically generate every valid bicycle configuration from a structured Excel file.

## Solution

This project provides a Python script that reads an Excel file containing all possible options for each bicycle part, generates all possible combinations, and outputs them as a JSON file. This makes it easy to manage, share, and use all bicycle configurations for manufacturing or sales.

## How the Code Works

- The script reads different sheets from the Excel file, each sheet describing a set of options (like frames, wheels, brakes, etc.).
- It finds all unique values for each part and generates every possible combination using these.
- For each combination, it collects all relevant details and creates a dictionary representing one bicycle configuration.
- All configurations are saved as a list in a JSON file called `output.json`.

You just need to run the script with your Excel file, and it will create a JSON file with all possible bicycle configurations.
