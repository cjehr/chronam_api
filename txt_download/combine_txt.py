import glob
import shutil

# Opens files in a directory and saves them to a single file with the file
# names included between file contents
# combined_YYYY.txt is the combined file name
count = 0
with open('combined_YYYY.txt', 'wb') as outfile:
    for filename in glob.glob('*.txt'):
        if filename == 'combined_YYYY.txt':
        
            continue
        with open(filename, 'rb') as readfile:
            name = str.encode('\n' + filename + '\n')
            count += 1
            outfile.write(name)
            shutil.copyfileobj(readfile, outfile)

print(str(count) + ' files combined')