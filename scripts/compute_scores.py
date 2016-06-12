'''
1. Compute scores from counts for each entry.

    score = max(count) - count / max(count)

    That is, score is the count normalized to be between 0 and 100 where 100
    indicates a count of 0 (best possible) and 0 the worse count (highest).

2. Compute scores for each place.

    Score for place = sum(score on place entries) / no risks where place has a score

3. Compute ranks for each place. Based on score.

4. Compute scores for each risk plus max, min counts, mean, median

5. Compute rank for each place on a risk
'''
import csv
from operator import itemgetter

risksfp = 'content/data/risks.csv'
entriesfp = 'content/data/entries.csv'
placesfp = 'content/data/places.csv'

entries_reader = csv.DictReader(open(entriesfp))
entries = [ row for row in entries_reader ]
for row in entries:
    row['count'] = int(row['count'])

risks_reader = csv.DictReader(open(risksfp))
risks = [ r for r in  risks_reader ]

places_reader = csv.DictReader(open(placesfp))
places = [ r for r in  places_reader ]

import math

def compute_scores():
    '''Compute scores for entries.
    '''
    for risk in risks:
        counts = [ entry['count'] for entry in entries if entry['risk'] == risk['id'] ]
        risk['max'] = max(counts)
        risk['min'] = min(counts)
        risk['total'] = sum(counts)
        risk['mean'] = risk['total'] / len(counts)
        risk['places_count'] = len(counts)

    risklookup = dict([ (risk['id'], risk) for risk in risks ])

    for entry in entries:
        risk = risklookup[entry['risk']]
        riskmax = float(risk['max'])
        score = math.log(float(entry['count'])) / math.log(riskmax)
        entry['score'] = round(100 * score, 2)

    for risk in risks:
        scores = [ entry['score'] for entry in entries if entry['risk'] == risk['id'] ]
        risk['score'] = int(round(sum(scores) / len(scores)))

    fieldnames = entries_reader.fieldnames
    writer = csv.DictWriter(open(entriesfp, 'w'), fieldnames)
    writer.writeheader()
    writer.writerows(entries)

    writer = csv.DictWriter(open(risksfp, 'w'), risks_reader.fieldnames)
    writer.writeheader()
    writer.writerows(risks)

    # print [ e['score'] for e in entries[0:50] ]

def place_scores_and_ranks():
    # scores
    for place in places:
        scores = [ entry['score'] for entry in entries if entry['place'] == place['id'] ]
        place['score'] = round(sum(scores) / len(scores), 2)

    # ranks
    add_ranks(places)
    # re-sort to original order
    places.sort(key=itemgetter('id'))
      
    writer = csv.DictWriter(open(placesfp, 'w'), places_reader.fieldnames)
    writer.writeheader()
    writer.writerows(places)

def add_ranks(ourlist):
    '''For a set of stuff with a score column, add rank based on score

    NOTE: operates in place on ourlist
    '''
    ourlist.sort(key=itemgetter('score'), reverse=True)
    rank = 1
    for idx, pl in enumerate(ourlist):
        pl['rank'] = rank
        if idx == (len(ourlist) - 1): # last item so can early exit
            continue
        if ourlist[idx+1]['score'] < pl['score']:
            rank = idx + 2
        else: # rank unchanged as a tie
            pass

def place_rank_per_risk():
    for risk in risks:
        entries_for_this_risk = [ e for e in entries if e['risk'] == risk['id'] ]
        add_ranks(entries_for_this_risk)

    entries.sort(key=lambda entry: (entry['risk'], entry['place'], entry['year']))

    fieldnames = entries_reader.fieldnames
    writer = csv.DictWriter(open(entriesfp, 'w'), fieldnames)
    writer.writeheader()
    writer.writerows(entries)


from nose.tools import assert_equals
def test_no_entries_with_same_rank_but_different_scores():
    for risk in risks:
        ourentries = [ e for e in entries if e['risk'] == risk['id'] ]
        ranks = dict([ (e['rank'], []) for e in ourentries ])
        for e in ourentries:
            ranks[e['rank']].append(e)
        for k,entrylist in ranks.items():
            if len(entrylist) > 1:
                for entry in entrylist:
                    assert_equals(entry['score'], entrylist[0]['score'])

def test_add_ranks():
    ourlist = [
        { 'name': 'a', 'score': 100.0 },
        { 'name': 'c', 'score': 10.0 },
        { 'name': 'b', 'score': 50.0 }
        ]
    add_ranks(ourlist)
    assert_equals(ourlist[0]['rank'], 1)
    assert_equals(ourlist[1]['rank'], 2)
    assert_equals(ourlist[2]['rank'], 3)
    assert_equals(ourlist[2]['name'], 'c')


if __name__ == '__main__':
    compute_scores()
    place_scores_and_ranks()
    place_rank_per_risk()

