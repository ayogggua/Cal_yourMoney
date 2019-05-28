class caculate_money(object):
	def __init__(self):
		self.basic = basic_money
		self.g1_hour = g1_hour
		self.g2_hour = g2_hour
		self.g3_hour = g3_hour
		self.quality_g1_hour = quality_g1_hour
		self.quality_g2_hour = quality_g2_hour
		self.quality_g3_hour = quality_g3_hour
		self.hour_money_hour = (float(self.basic_money) / 21.75) / 8

	def g1(self,g1_hour):
		g1 = float(g1_hour) * 1.5 * float(self.hour_money)
		print ('g1 money = ',g1)
		return g1

	def g2(sllf,g2_hour):
		g2 = g2_hour * 2 * float(self.hour_money)
		print ('g2 money = ',g2)
		return g2

	def g3(self,g3_hour):
		g3 = g3_hour * 3 * float(self.hour_money)
		print ('g3 money = ',g3)
		return g3

	def quanlity_g1(self,quanlity_g1_hour):
		qg1 = quanlity_g1 * 1.5 * float(self.hour_money)
		print ('quanlity G1 = ',qg1)
		return qg1

	def quanlity_g2(self,quanlity_g2_hour):
		qg2 = quanlity_g2 * 1.5 * float(self.hour_money)
		print ('quanlity G2 = ',qg2)
		return qg2

	def quanlity_g3(self,quanlity_g3_hour):
		qg3 = quanlity_g3 * 1.5 * float(self.hour_money)
		print ('quanlity G3 = ',qg3)
		return qg3

	def sum_money(self):
		sum_money = self.basic + self.g1 + self.g2 + self.g3 + self.qg1 + self.qg2 + self.qg3
		print ('sum_money = ',sum_money)
		return sum_money