#!/usr/bin/env python
"""
Alice has the following two types of taxis:

- Online taxi: It can be booked by using an online application from phones
- Classic taxi: It can be booked anywhere on the road
 
The online taxis cost O_c for the first O_f km and O_d for every km afterward. 
The classic taxis travel at a speed of C_s km per minute. The cost of classic 
taxis are C_b, C_m and C_d that represents the base fare, cost for every minute 
that is spent in the taxi, and cost for each kilometer that you ride.

You are going to the office from your home. Your task is to minimize the cost 
that you are required to pay. The distance from your home to the office is D. 
You are required to select whether you want to use online or classic taxis to 
go to your office. If both the taxis cost the same, then you must use an online 
taxi.

INPUT
-----
- First line: Single integer D that denotes the distance from your house to the 
  office
- Next line: Three integers O_c, O_f, and O_d.
- Next line: Four integers C_s, C_b, C_m, and C_d.
  
OUTPUT
------
If you select an online taxi to travel, then print a string 'Online Taxi'. Otherwise, 
select 'Classic Taxi'. You can print this string in a new, single line.

CONSTRAINTS
-----------
1 <= D, O_c, O_f, O_d, C_s, C_b, C_m, C_d <= 10^9
"""

__author__ = "Cristian Chitiva"
__date__ = "September 18, 2023"
__email__ = "cychitivav@unal.edu.co"

D = int(input())
O_c, O_f, O_d = list(map(int, input().split()))
C_s, C_b, C_m, C_d = list(map(int, input().split()))

O_cost = O_c + (D - O_f) * O_d if D > O_f else O_c
C_cost = C_b + (D / C_s) * C_m + D * C_d

print("Online Taxi" if O_cost < C_cost else "Classic Taxi")
