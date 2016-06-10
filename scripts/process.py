#!/usr/bin/python
# -*- coding: utf8 -*-
import os
from os.path import join
import csv

DATAPATH = 'content/data'
PLACEPATH = 'content/pages/place'
PLACESFILE = os.path.join(DATAPATH, 'places.csv')
RISKSFILE = os.path.join(DATAPATH, 'risks.csv')
ENTRIESFILE = os.path.join(DATAPATH, 'entries.csv')


def create_content(output_dir=PLACEPATH):
    '''Creates content for every place and every risk in that place
    
    '''
    fo = open(PLACESFILE)
    places = [ place for place in csv.DictReader(fo) ]

    fo = open(RISKSFILE)
    risks = [ r for r in csv.DictReader(fo) ]

    place_template = \
'''type: place
template: place
title: %(name)s
slug: place/%(slug)s
place: %(id)s
year: 2016'''
    risk_template = \
'''type: place_risk
template: place_risk
title: %s/%s
slug: place/%s/%s
place: %s
risk: %s
year: 2016
'''
    for place in places:
        place_dir = join(output_dir, place['id'])
        if not os.path.exists(place_dir):
            os.mkdir(place_dir)

        text = place_template % place
        place_writefile = open(join(place_dir, 'index.md'), 'w')
        place_writefile.write(text)

        for risk in risks:
            risk_dir = join(place_dir, risk['id'])
            if not os.path.exists(risk_dir):
                os.mkdir(risk_dir)
            risk_writefile = open(join(risk_dir, 'index.md'), 'w')
            text = risk_template % (place['name'], risk['id'], place['slug'], risk['id'], place['id'], risk['id'])
            risk_writefile.write(text)
            risk_writefile.close()


import tempfile
import shutil
import random
def test_create_content():
    tmpdir = tempfile.mkdtemp()
    create_content(tmpdir)
    
    fo = open(PLACESFILE)
    places = [ place for place in csv.DictReader(fo) ]
    fo = open(RISKSFILE)
    risks = [ r for r in csv.DictReader(fo) ]
    
    for place in places:
        assert(os.path.exists(tmpdir + '/' + place['id'] + '/index.md'))
        for risk in risks:
            assert(os.path.exists(tmpdir + '/' + place['id'] + '/'+ risk['id'] + '/index.md'))
    
    random_place = random.choice(places)
    fo = open(tmpdir + '/' + random_place['id'] + '/index.md')
    test_template = ''
    result = \
'''type: place
template: place
title: %(name)s
slug: place/%(slug)s
place: %(id)s
year: 2016''' % (random_place)
    for line in fo:
        test_template += line
    assert(test_template == result)
    
    random_risk = random.choice(risks)
    fo = open(tmpdir + '/' + random_place['id'] + '/' + random_risk['id'] +  '/index.md')
    test_template = ''
    result = \
'''type: place_risk
template: place_risk
title: %s/%s
slug: place/%s/%s
place: %s
risk: %s
year: 2016
''' % (random_place['name'], random_risk['id'], random_place['slug'], random_risk['id'], random_place['id'], random_risk['id'])
    for line in fo:
        test_template += line
    assert(test_template == result)
    shutil.rmtree(tmpdir)
    
if __name__ == '__main__':
    test_create_content()
    create_content()
