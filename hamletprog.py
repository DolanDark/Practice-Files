import collections
import matplotlib.pyplot as plt

hamlet = '''To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die—to sleep,
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to: 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep, perchance to dream—ay, there's the rub:
For in that sleep of death what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause—there's the respect
That makes calamity of so long life.
For who would bear the whips and scorns of time,
Th'oppressor's wrong, the proud man's contumely,
The pangs of dispriz'd love, the law's delay,
The insolence of office, and the spurns
That patient merit of th'unworthy takes,
When he himself might his quietus make
With a bare bodkin? Who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscovere'd country, from whose bourn
No traveller returns, puzzles the will,
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience doth make cowards of us all,
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry
And lose the name of action.'''

dic1 = {}
for i in hamlet:
    if i in dic1:
        dic1[i] = dic1[i] + 1
    else:
        dic1[i] = 1

print(dic1)
X,Y = zip(*dic1.items())
plt.bar(X, Y)
plt.show()

dic2 = {}
for j in hamlet:
    dic2[j] = dic2.get(j, 0)+1
print(dic2)
plt.bar(dic2.keys(), dic2.values())
plt.show()

count = collections.Counter(hamlet)
print(count)

plt.bar(count.keys(), count.values())
plt.show()

