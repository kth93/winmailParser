import sys
import struct

WINMAIL_SIGNATURE = 0x223e9f78

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: winmailParser.py [File]')
        sys.exit(0)
    
    fileName = sys.argv[1]

    fp = open(fileName, 'rb')
    signature = struct.unpack('<I',fp.read(4))[0]

    if signature == WINMAIL_SIGNATURE:    
        print('This is TNEF Format')
