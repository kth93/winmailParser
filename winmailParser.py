import sys
import struct

WINMAIL_SIGNATURE = 0x223e9f78
ATTACHMENT_DATA = 0x800F
ATTACHMENT_NAME = 0x8010
ATTACHMENT_OFFSET = 0x9002
ATTACHMENT_PROPS = 0x9005
MESSAGE_PROPS = 0x9003

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: winmailParser.py [File]')
        sys.exit(0)
    
    fileName = sys.argv[1]

    fp = open(fileName, 'rb')
    buf = fp.read()
    fp.close()
    signature = struct.unpack('<I', buf[:4])[0]

    if signature == WINMAIL_SIGNATURE:    
        print('This is TNEF Format')

    attachKey = struct.unpack('<H', buf[4:6])[0]

    print(attachKey)
