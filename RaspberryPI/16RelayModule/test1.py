# Author: Expert Ngobeni
# Date: 21 April 2018
# Company: Expert Cyclone
# Title: 16 Relays Module Testing

# Import Modules
from gpiozero import LED
from time import sleep

# Control Flags
ENABLE      = 0
DISABLE     = 1

# Pin Mapping
A1 = LED(5)
A2 = LED(6)
A3 = LED(13)
B1 = LED(19)
B2 = LED(26)
B3 = LED(20)

# Switch a pin on/off
A1.value    = ENABLE
A2.value    = DISABLE
A3.value    = ENABLE
B1.value    = DISABLE
B2.value    = DISABLE
B3.value    = DISABLE



