import os
import shutil
from pathlib import Path
from datetime import datetime
import threading

source_path = input('Enter path for folder "Source":')
replica_path = input('Enter path for folder "Replica:')
log_file_path = input('Enter path for your Log text file:')
sync_interval = int(input('Enter synchronization interval (in seconds):'))

def sync():

    timestamp = datetime.today()
    log_file = open(log_file_path, 'a')

    #Below loop designed to copy files that are in Source but not in Replica
    os.chdir(source_path)
    for filename in os.listdir(source_path):
        if filename not in os.listdir(replica_path):
            shutil.copy(str(os.path.abspath(filename)),os.fspath(replica_path)) 
            log_file.write(f'{timestamp} - {filename} has been copied to Replica.\n')
            print(f'{timestamp} - {filename} has been copied to Replica.')
        else:
            pass
    
    #Below loop designed to remove files that are in Replica but not in Source (one-way synchronization)      
    os.chdir(replica_path)
    for filename in os.listdir(replica_path):
        if filename in os.listdir(source_path):
            pass
        else: 
            os.remove(str(os.path.abspath(filename)))
            log_file.write(f'{timestamp} - {filename} has been removed from Replica.\n')
            print(f'{timestamp} - {filename} has been removed from Replica.')

    log_file.close()

    threading.Timer(sync_interval, sync).start() #Setting up the synchronization interval

sync()