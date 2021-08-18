# Self Destruct timer adjustment
# This python file will adjust the self destruct timer for all playfields it finds
# within the current directory, including subdirectories. It will backup the files
# if it changes them. If a backup already exists, it will overwrite the backup.

import yaml
import argparse

parser = argparse.ArgumentParser('Update self-destruct settings across all playfields')
parser.add_argument('Target directory', 
  help='Target Playfield directory - will recurse!')
parser.add_argument('--self-destruct-min-timeout', dest='timeout', type=int, default=1800, 
  help='Minimum timeout for self-destruct, in seconds. Default is 1,800 (30 minutes)')
parser.add_argument('--self-destruct-max-delta', dest='delta', type=int, default=900,
  help='Maximum delta for self-destruct, in seconds. Default is 900 (15 minutes)')
parser.add_argument('--military-immediate-destruct', dest='military', default='False', choices=['True','False'],
  help='Military ships immediately start self destruct. True/False. Default is False')
parser.add_argument('--overwrite-backup', dest='overwrite', default='True', choices=['True','False'],
  help='Overwrite backup files that already exist. Otherwise do not create backup. True/False. Default is True')
parser.add_argument('--backup-extension', dest='extension', default='backup',
  help='Backup file extension. Default is .backup')

args = parser.parse_args()

print(args)

# Validate inputs

# Traverse target
# Read each playfield yaml
# Search for military true/false
# Search for minimum/maximum
