import re

f = open('input_day02.txt', 'r')

squareFeetOfWrappingPaper = 0
feetOfRibbon = 0

for line in f:
    l, w, h = map(
        lambda x: int(x),
        re.search('(?P<l>\d+)x(?P<w>\d+)x(?P<h>\d+)', line).groups()
    )
    side1 = l * w
    side2 = w * h
    side3 = h * l
    squareFeetOfWrappingPaper += 2 * (side1 + side2 + side3) + min(side1, side2, side3)

    dimensions = [l, w, h]
    smallest = min(dimensions)
    dimensions.remove(smallest)
    secondSmallest = min(dimensions)
    feetOfRibbon += (2 * smallest) + (2 * secondSmallest) + (l * w * h)

print 'squareFeetOfWrappingPaper: ', squareFeetOfWrappingPaper
print 'feetOfRibbon: ', feetOfRibbon
