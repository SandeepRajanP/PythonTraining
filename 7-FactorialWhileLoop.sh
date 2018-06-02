#!/bin/bash

echo "Input a number to find the factorial of it:"
read NUM
A=1
FACT=1
while [ $A -le $NUM ]
do
    FACT=$( expr "$A" '*' "$FACT")
    A=$((A+1))
done
echo "Factorial:" $FACT
