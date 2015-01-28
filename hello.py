#!/usr/bin/env python

a = "Once upon a time, a family of %d bears lived in the woods." % 3
mamabear = "Mrs. Bear"
papabear = "Mr. Bear"
babybear = "Lil Fuzzy"
b = "Their names were %s, %s and %s." % (mamabear, papabear, babybear)

print a
print b

x = 3
y = x+2

print "One day, the", x, "bears encountered another, larger family of", y, "bears while cavorting around the wilderness."


z = x + y

print "The %d families converged upon a grove of backscratching trees." % 2
print "To their horror, they discovered that their were", z, "bears and only %d trees." % 7

print "'Oh No,'", mamabear,"cried out. 'However will we all adequately scratch our backs?'"

t = z % 7

print "The bears knew there would be %r bear left out of backscratching." % t

v = z / 2

print "So they decided to combine the %d families and arbitrarily divide them into new families of %r for the purposes of fairness." % (2, v)

tug = "tug of war"
brawl = "boxing match"

print "They initially considered settling things with a %r on %r %s." % (v, v, brawl)
print "But finally, they settled on a more peaceful %s." % tug
print "The winning team, being composed of members of either family, would have to come to a mutual agreement on allotting the remaining %r trees to the losers." % (v - 1 )
print "But such diplomacy was unnecessary. Almost immediately,", babybear,"tugged so hard that he slipped free from the rope and tumbled off the side of a ravine, never to be seen again."
u = 7 % 7
print "The bears rejoiced, for each was now secure in his or her possession of a scratching tree."
print "~~~~!!!!~~~~THE ~~ END ~~~~!!!!~~~~"


