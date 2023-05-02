# Sets
# set is creating by {}
#
SetA:set={'python',1,23,3,4,5,6,7,8,9};
print(SetA);
set1=set([1,2,3,4,5]);
print(set1);
setB=set();
setB={1,2,3,4,5,6,7,8,'Bangladesh'};
print(type(setB));
setC={}
print(type(SetA));

#all sets function()
'''
add()
clear()
update()
discard()
remove()
union()
intersection()
difference()
symmentric_difference()
pop()
isdisJoint()
issubset()
issuperset()
'''
SetA.add(10.0);
SetA.add(20.00);
print(SetA);

AllClear=SetA.clear();
print(AllClear);

UpDateSet=SetA.update([1,2,3,4,5,6]);
print(UpDateSet);
print(SetA);

# discard
SetA.discard(3)
SetA.discard(4)
print(SetA);
#remove
SetA.remove(6);
print(SetA)
SetAA={1,2,3,4,5,6,7,8}
SetBB={3,4,5,6,10,11,12}
##Union()
unionIs=SetA.union(SetBB);
print(unionIs);
##union()
##intersection()
IntersectionIs=SetAA.intersection(SetBB);
print(IntersectionIs);
##difference()
Difference=SetAA.difference(SetBB)
print(Difference);
##symmentric_difference()
Sysemmemctic_differenec=SetAA.symmetric_difference(SetBB);
print(Sysemmemctic_differenec);
##pop()
poping=SetAA.pop()
print(SetAA.pop())
print(SetAA);

##isdisJoint()
IsJoinging=SetAA.isdisjoint(SetBB);
print(IsJoinging);
##issubset()
IsSubSet=SetAA.issubset(SetBB);
print(IsSubSet);
##issuperset()
IsSuperSet=SetAA.issuperset(SetBB);
print(IsSuperSet);
print(2 in SetAA);
print(3 not in  SetBB);
##Sorted
setE={6,7,1,2,10,9,'python'}
for x in setE:
    print(x);