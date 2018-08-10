
from __future__ import unicode_literals
from collections import OrderedDict

from .. import Provider as MedicationProvider


class Provider(MedicationProvider):
	 # Add data
	brand = (
		'Advil',
		'Tylenol',
		'Motrin',
		''
	)
	generic = (
		'acetomenaphin',
		'generic drug name',
		'another generic drug name',
		''
	)
	compound = (
		'Acetomenaphin',
		'Ibuprofin',
		'acetomenaphin',
		'ibuprofin',
		''
	)
	dosage = (
		'200mg',
		'500mg',
		'2 capsules',
		'',
		'100mg BID',
		'50mg'
	)
	medication_formats = (
		'{{brands}} {{generics}}',
		'{{brands}}-{{generics}}',
		'{{brands}}, {{generics}} and {{dosages}}',
		'{{brands}}',
		'{{generics}}',
		'{{compounds}}',
		'{{dosages}} {{brands}}',
		'{{generics}} {{dosages}}'
	)


'''
Notes:

Formats get function calls in abstracted class
Data specific to individual subtypes get put in here


'''