from cal_main import caculate_money
user = caculate_money()
user.g1_hour = input('please input your G1 hours:')
user.g1(g1_hour)
user.g2_hour = input('please input your G2 hours:')
user.g2(g2_hour)
user.g3_hour = input('please input your G3 hours:')
user.g3(g3_hour)
user.quality_g1_hour = input('please input your quality_g1 hours:')
user.quality_g1(quality_g1_hour)
user.quality_g2_hour = input('please input your quality_g2 hours:')
user.quality_g2(quality_g2_hour)
user.sum_money()