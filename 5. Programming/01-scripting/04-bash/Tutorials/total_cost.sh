#!/bin/bash 

# In this exercise, you will need to calculate the total cost (variable TOTAL) of a fruit basket, which contains: 1 pineapple, 2 bananas and 3 watermelons. Don't forget to include the cost of the basket....

COST_PINEAPPLE=50

COST_BANANA=4

COST_WATERMELON=23

COST_BASKET=1

TOTAL=$(($COST_PINEAPPLE + $COST_BANANA * 2 + $COST_WATERMELON * 3 + $COST_BASKET))

echo "Total Cost is $TOTAL"