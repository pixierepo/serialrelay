# serialrelay
Simple class for controling a USB Serial Relay board

# Usage:

```
# import and create your relay object (if device is not '/dev/ttyUSBX', pass the name as param).
import serialrelay

myrelay = serialrelay.SerialRelay()

## To close the relay:
myrelay.close()

## To open the relay:
myrelay.open()

## To close for 3 seconds and open again:
myrelay.toggle()

```

Class is very simple, explore for other features.
