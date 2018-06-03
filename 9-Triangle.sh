#!/bin/bash

echo "Input three integers as the sides of a triangle"
read A
read B
read C

if [[ ( $(($A + $B)) -gt $C ) &&  ( $(($B + $C)) -gt $A )  &&  ( $(($C + $A)) -gt $B ) ]]
then 
	if  [[ ( $A -eq $B ) && ( $A -eq $C ) ]]
	then
		echo "The Triangle is Equilateral"
	elif [[ ( $A -eq $B ) || ( $A -eq $C ) || ( $B -eq $C ) ]]
	then	
		echo "The Triangle is Isoceles"
	else
		echo "The Triangle is Scalene"
	fi
else
	echo "The three integers won't represent the sides of a triangle...Try again"
fi	
