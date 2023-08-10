def overheads_function():
    from pathlib import Path
    import csv

    fp = Path.cwd()/'csv_reports'/"Overheads.csv"
    # print(fp.exists())   - To check if file is present

    overheads = [] #create an empty list.
# append overhead data to empty list.
    with fp.open(mode='r', encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            overheads.append({'Category': row[0], 'Amount': float(row[1])})

    # print(overheads)   #-To check through the data 
# this function is used to find the highest overhead.
    def highest_overhead_category(overheads):
        """
        - To find the highest overhead category and highest overhead value.
        - Parameter required: overheads
        """
        max_overhead = 0
        highest_category = None

        for row in overheads:
            overhead = row['Amount']
            if overhead > max_overhead:
                max_overhead = overhead
                highest_category = row['Category']

        return highest_category, max_overhead #output of highest overhead returned.

    folder_path = Path.cwd() / 'csv_reports' #create a file to csv file
    file_name = 'overheads.csv'
    file_path = folder_path / file_name
    # print(file_path.exists()) # check if file exists

    highest_category, max_overhead = highest_overhead_category(overheads)

    highest_category = highest_category.upper()

    return highest_category, max_overhead


