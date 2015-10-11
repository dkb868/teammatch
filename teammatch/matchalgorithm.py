#!/usr/bin/env python
def score( hacker, profile ):
    ''' Returns score based on how close profile is to what is wanted'''


    hlang = hacker.languages_wanted
    plang =  profile.languages_well
    plang2 = profile.languages_bad
    score = 0.0
    for h in platforms_wanted:
        for p in platforms_mentee:
            if h == p:
                score+= 1.0
    for h in hlang:
        for p in plang:
            if h == p:
                score+= 1.0

        for p in plang2:
            if h == p:
                score += 0.5
    score /= 2

    #hyr = hacker.year
    #pyr = profile.year
    #score += (3 - abs(hyr-pyr))

    hgenre = hacker.genre
    pgenre = profile.genre
    if hgenre == pgenre:
        score += 2

    htype= hacker.type
    ptype = profile.type
    if htype == ptype:
        score += 2

    hcomp = hacker.iscompetitive
    pcomp = profile.iscompetitive
    if hcomp == pcomp:
        score += 2
        


    return score

def matches( hacker, profiles ):
    '''Returns list of profiles with best matches first'''
    results = []
    for profile in profiles:
        results.append( (score(hacker,profile), profile ))
    results = sorted( results, key=lambda score: score[0])[:-1]
    return results

class Hacker:
    def __init__(self, lang, genre, platforms, iscomp):
        self.languages_wanted = lang
        self.genre = genre
        self.platforms = platforms
        self.iscompetitive = iscomp

class Profile:
    def __init__(self, name, langwell, langbad, genre, platforms, iscomp, id):
        self.name = name
        self.languages_well = langwell
        self.languages_bad = langbad
        self.genre = genre
        self.platforms = platforms
        self.iscompetitive = iscomp
        self.id = id
