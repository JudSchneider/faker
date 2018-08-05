# coding=utf-8

from __future__ import unicode_literals
from .. import BaseProvider


class Provider(BaseProvider):
    formats = {
        '{{brand}} {{generic}}',
        '{{brand}}-{{generic}}',
        '{{brand}}, {{generic}} and {{dosages}}',
        '{{brand}}',
        '{{generic}}',
        '{{compound}}',
        '{{dosages}} {{brand}}',
        '{{generic}} {{dosages}}'
    }
    # Add data
    brand = {
    		'Advil',
    		'Tylenol',
    		'Motrin',
    		''
    }
    generic = {
    		'acetomenaphin',
    		'generic drug name',
    		'another generic drug name',
    		''
    }
    compound = {
    		'Acetomenaphin',
    		'Ibuprofin',
    		'acetomenaphin',
    		'ibuprofin',
    		''
    }
    dosages = {
    		'200mg',
    		'500mg',
    		'2 capsules',
    		'',
    		'100mg BID',
    		'50mg'

    }
    # Store needed data here

    def medication(self):
        '''
        example = lortab
        '''
        pattern = self.random_element(self.formats)
        return self.generator.parse(pattern)

