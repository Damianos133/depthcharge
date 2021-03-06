#!/usr/bin/env python3
import traceback
from depthcharge import Console, Depthcharge, log

ctx = None

try:
    console = Console('/dev/ttyUSB0', baudrate=115200)
    ctx = Depthcharge(console)

    # Perform actions here

except Exception as error:
    log.error(str(error))

    # Shown if DEPTHCHARGE_LOG_LEVEL=debug in environment
    log.debug(traceback.format_exc())

finally:
    # Save gathered information to a device configuration file
    if ctx:
        ctx.save('my_device.cfg')
