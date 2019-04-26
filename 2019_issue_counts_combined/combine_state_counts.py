import glob
import shutil

# Opens .csv files in a directory and appends them to a single file.
# combined_state_count.csv is the combined file name.

count = 0
with open('combined_state_count.csv', 'wb') as outfile:
    for filename in glob.glob('*.csv'):
        if filename == 'combined_state_count.csv':
            continue
        with open(filename, 'rb') as readfile:
            count += 1
            shutil.copyfileobj(readfile, outfile)

print(str(count) + ' files combined')