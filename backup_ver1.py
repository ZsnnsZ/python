import os
import time
source = 'C:\\test1'
target_dir = 'C:\\test2\\'
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = input('Enter a comment--> ')
if len(comment) == 0:
    target = today + os.sep + now + '.rar'
else:
    target = today + os.sep + now + '_' + comment.replace(' ','_') + '.rar'

if not os.path.exists(today):
    os.mkdir(today) # make directory
    print ('Successfully created directory', today)

rar_command = '"C:\\Program Files\\WinRAR\\WinRAR.exe" A %s %s -r' % (target,source)

if os.system(rar_command) == 0:
    print ('Successful backup to', target)
else:
    print ('Backup FAILED')
