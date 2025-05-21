# SET OPERATIONS – Book Club Example

# Members who read in January
january_readers = {"Alice", "Bob", "Charlie", "Diana"}

# Members who read in February
february_readers = {"Charlie", "Eve", "Bob", "Frank"}

# Members who read in both January and February
both_months = january_readers.intersection(february_readers)
print("Read in both months:", both_months)

# Members who read only in January
only_january = january_readers.difference(february_readers)
print("Only January:", only_january)

# All unique readers across both months
all_readers = january_readers.union(february_readers)
print("Total unique readers:", all_readers)

# Members who did not read in February
not_february = january_readers - february_readers
print("Did not read in February:", not_february)
