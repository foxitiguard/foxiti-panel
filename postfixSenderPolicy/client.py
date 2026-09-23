#!/usr/local/FoxitiCP/bin/python
import socket
import sys
sys.path.append('/usr/local/FoxitiCP')
from plogical.FoxitiCPLogFileWriter import FoxitiCPLogFileWriter as logging
import argparse
from plogical.mailUtilities import mailUtilities

class cacheClient:
    cleaningPath = '/home/foxitipanel/purgeCache'

    @staticmethod
    def handleCachePurgeRequest(command):
        try:
            mailUtilities.checkHome()
            writeToFile = open(cacheClient.cleaningPath, 'w')
            writeToFile.write(command)
            writeToFile.close()

        except BaseException as msg:
            logging.writeToFile(str(msg) + ' [cacheClient.handleCachePurgeRequest]')


def main():

    parser = argparse.ArgumentParser(description='foxitiPanel Email Policy Cache Cleaner')
    parser.add_argument('function', help='Specific a function to call!')


    args = parser.parse_args()

    if args.function == "hourlyCleanup":
        command = 'foxitipanelCleaner hourlyCleanup'
        cacheClient.handleCachePurgeRequest(command)
    elif args.function == 'monthlyCleanup':
        command = 'foxitipanelCleaner monthlyCleanup'
        cacheClient.handleCachePurgeRequest(command)


if __name__ == "__main__":
    main()