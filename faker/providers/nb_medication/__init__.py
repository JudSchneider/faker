# coding=utf-8

from __future__ import unicode_literals
from .. import BaseProvider

localized = True

class Provider(BaseProvider):

	brand = ['Claritin',]
	generic = ['salbutamol',]
	compound = ['slbutamol citrate',]
	dosage = ['500mg', ]
	medication_formats = (
		'{{brands}} {{generics}}',
	)
	quantity = ['2', 'NULL','150','5','NULL']
	route_concept = ['4128794','4184551','0','4112421']
	route_source = ['ORAL','EACH EYE','BY_MOUTH','NULL','PO','','subdurmal','translingual']
	dosage_unit = ['miligram','NULL','puffs','mililiter']
    # Store needed data here
	def brands(self):
		return self.random_element(self.brand)

	def generics(self):
		return self.random_element(self.generic)

	def compounds(self):
		return self.random_element(self.compound)

	def dosages(self):
		return self.random_element(self.dosage)

	def drug_source_value(self):
		'''
		example = lortab
		'''
		pattern = self.random_element(self.medication_formats)
		return self.generator.parse(pattern)

	def drug_exposure_id(self):
		return "%08d" % self.generator.random.randint(1111111, 99729999)

	def drug_quantity(self):
		return self.random_element(self.quantity)

	def route_concept_id(self):
		return self.random_element(self.route_concept)

	def drug_route_source_value(self):
		return self.random_element(self.route_source)

	def drug_source_concept_id(self):
		return "%06d" % self.generator.random.randint(0, 929999)

	def dose_unit_source_value(self):
		return self.random_element(self.dosage_unit)

'''
Functions in here are called in the medication formats
individual data points added here are consistent across all classes


'''