class caculate_money(object):
	def __init__(self, basic_money, g1, g2, g3, quality_g1, quality_g2, quality_g3):

		self.basic = basic_money
		self.g1 = g1
		self.g2 = g2
		self.g3 = g3
		self.quality_g1 = quality_g1
		self.quality_g2 = quality_g2
		self.quality_g3 = quality_g3
		self.hour_money = (self.basic / 21.75) / 8

	def g1(self,g1_hour):
		g1 = g1_hour * 1.5 * self.hour_money
		return g1
	