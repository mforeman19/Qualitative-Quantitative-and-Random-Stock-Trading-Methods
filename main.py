from qualitative_bot import qualitativeBot
from random_bot import randomBot
from quantitative_bot import quantitativeBot

for i in range(0,3):

    qualB = qualitativeBot()
    rb = randomBot()
    quantB = quantitativeBot()

    qualB.select()
    rb.select()
    quantB.select()

    print("Qualitative: ", qualB.getSelections())
    print("Qualitative Beginning: ", qualB.getBeginning())
    print("Qualitative End: ", qualB.getEnd())
    print("Qualitative Diff: ", qualB.getDifference())

    print("Random: ", rb.getSelections())
    print("Random Beginning: ", rb.getBeginning())
    print("Random End: ", rb.getEnd())
    print("Random Diff: ", rb.getDifference())

    print("Quantitative: ", quantB.getSelections())
    print("Quantitative Beginning: ", quantB.getBeginning())
    print("Quantitative End: ", quantB.getEnd())
    print("Quantitative Diff: ", quantB.getDifference())
