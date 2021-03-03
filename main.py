# Libraries
from datetime import datetime as dt 
from datetime import timedelta as td 

# Parameters 
ROOTDIR = "./data/"
TIME_OFFSET = 10
SEGMENT_AMOUNT = 23 
CHANNEL = ['WV073', 'WV069','WV063','VI008','VI005','VI004','SW038','NR016','NR013','IR133','IR123','IR112','IR105','IR096','IR087','VI006']
current_target_path = ""
target_path = "NA"
expected_filelist = [] 

# Nameclature
filename_pattern = "type_seq_ch_yyyymmddHHMM3600_seg.uhrit" 

# Set target folder 
target_dt = (dt.utcnow() - td(minutes=TIME_OFFSET)).strftime("%Y%m%d%H%M")[0:11] + "7"
target_date_folder = target_dt[0:4] + '-' + target_dt[4:6] + '-' + target_dt[6:8]
target_time_folder = target_dt[8:10] + '-' + target_dt[10:12]
target_path = ROOTDIR + target_date_folder + '/' + target_time_folder + '/'
print(target_path)

# Set expected file list 
if current_target_path != target_path : 
    current_target_path = target_path
    # record all missing segments 
    expected_filelist = [filename_pattern.replace("yyyymmddHHMM", target_dt).replace("ch", channel).replace("seg",seg) for channel in CHANNEL for seg in range(1,24)]
    

# Find each file in the list in target folder

# Remove them from list after found them 

# Do this action until either list is empty or target folder updates. Generate a table. 
# if list is empty, sleep until target folder updates

