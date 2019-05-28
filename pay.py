#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-29 00:21:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

print('calculation your Money')

basic_money = float(input('plesae your basic money'))
g1_hours = float(input('please your g1 overtime hours'))
g2_hours = float(input('please your g2 overtime hours'))
g3_hours = float(input('please your g3 overtime hours'))
quality_g1_hour = float(input('please your quality g1 overtime hours'))
quality_g2_hour = float(input('please your quality g2 overtime hours'))
quality_g3_hour = float(input('please your quality g3 overtime hours'))
hour_money = basic_money / 21.75 / 8

print ('you hour money is ',hour_money)
g1_money = hour_money * g1_hours * 1.5
print ('you g1 overtime money is ',g1_money)
g2_money = hour_money * g2_hours * 2
print ('you g1 overtime money is ',g1_money)

g3_money = hour_money * g3_hours * 3
print ('you g1 overtime money is ',g3_money)

quality_g1_money = hour_money * quality_g1_hour * 1.5
print ('you quality g1 money is ',quality_g1_money)

quality_g2_money = hour_money * quality_g2_hour * 2
print ('you quality g1 money is ',quality_g2_money)

quality_g3_money = hour_money * quality_g3_hour * 3
print ('you quality g1 money is ',quality_g3_money)

sum_money =basic_money + g1_money + g2_money + g3_money + quality_g1_money + quality_g2_money + quality_g3_money
print ('sum_money is',sum_money)
