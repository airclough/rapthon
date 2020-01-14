import sys
import time

sys.path.append( '.' )
sys.path.append( '..' )
sys.path.append( '../..' )

from Hologram.HologramCloud import HologramCloud

def popReceivedMessage():
    recv = hologram.popReceivedMessage()
    if recv is not None:
        print( str( recv ) )

def handle_polling( timeout, fx, delay_interval = 0 ):
    try:
        if timeout != -1:
            print( 'Timeout: ' + str(timeout) )
            end = time.time() + timeout
            while time.time() < end:
                fx()
                time.sleep( delay_interval )
        else:
            while True:
                fx()
                time.sleep( delay_interval )
    except KeyboardInterrupt as e:
        sys.exit( e )

if __name__ == '__main__':
    print( 'Rapthon running' )
    device_key = '=UNVe7vK'
    credentials = { 'devicekey': device_key }
    hologram = HologramCloud( credentials, network = 'cellular', authentication_type = 'csrpsk' )

    hologram.openReceiveSocket()
    print( 'Ready to receive data' )
    handle_polling( 50, popReceivedMessage, 1 )
    hologram.closeReceiveSocket()
