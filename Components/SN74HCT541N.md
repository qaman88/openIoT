# SN74HCT541N

Control output from input and output-enable.

## Applications

- Logic switches
- Main switch

## Switch: Input to output driver

- Inputs:  A1 to A8
- Outputs: Y1 to Y8

## Main Switches: Output-Enable (OE)

- OS1 if high all outputs (Y1 - Y8) are disconnected (high-impedance)
- OS2 if high all outputs (Y1 - Y8) are disconnected (high-impedance)
- OS1 or OS1 disconnects outputs without regards to inputs (A1 -A8) states

## Truth Table

```js
OE1^ | OE2^ |   A   |   Y   |
-----------------------------
0    |  0   |   0   |   0   |
0    |  0   |   1   |   1   |
1    |  X   |   X   |   Z   |
X    |  1   |   X   |   Z   |
```

## Power

- VCC = 4.5 to 5.5 V
- GND = 0 V
- A   = VCC
- Y   = VCC
- OE  = VCC
- 