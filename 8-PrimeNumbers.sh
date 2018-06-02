#!/bin/bash

for i in {1..100}
do
	count=0
	for j in $(seq 2 $((i/2))) 
	do
		if [ $(($i%$j)) -eq 0 ]
		then
			count=1
			break

		fi	
	done
	[ $count -eq 0 ] && echo $i
done		
