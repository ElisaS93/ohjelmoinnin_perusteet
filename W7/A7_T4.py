# T4 - Timestamp dataclass (TEST TASK)
# Structure timestamp data in program.

# This task is continuation to the A7_T3 task. You may start this task by copying the previous datasets. Rename datasets to match this task e.g., “A7_T3_D1.csv” => “A7_T4_D1.csv”.

# The dataset had four different values separated by a semicolon ;:

# Weekday
# Hour
# Consumption(kWh)
# Price(€/kWh)
# The goal is to print each timestamp from a file and also calculate the total of consumption and price. Below is the output format for a single record.

# Electiricity usages:
# - Monday 12:00, price 0.20 €, consumption 15.00 kWh, total 3.00 €
# - ...
# To keep the code maintainable, define a named datastructure for the different values. Once defined, specify a way to read the timestamps into a list. This can be done by reading a file line by line, skipping empty lines, trimming line endings, and then splitting each line by the delimiter.

# Code example of the operations:

# # Constants
# DELIMITER = ";"
#   # iterate over lines
#     ...
#     Row = Line.rstrip()               # Remove newline
#     Columns = Row.split(DELIMITER)      # Splits the row into a list
#     Timestamp = TIMESTAMP()           # Create object
#     Timestamp.weekday = Columns[0]      # Collect the first column
#     ...                               # Collect rest of the columns...
#     Timestamp.price = float(Columns[3]) # Collect the fourth column and convert datatype
#     Columns.clear()
# Preferred datastructures:

# Timestamps: list[TIMESTAMP]