
import matplotlib.pyplot as plt
import pandas as pd


fig = plt.figure()

rect = fig.patch
rect.set_facecolor('#E6D5FF')

df = pd.read_csv('Wiimmfi_Numbers.csv')

graph1 = fig.add_subplot(1, 1, 1, axisbg='white')

graph1.plot()
pd.DataFrame.plot(df)
xAx = list(range(0, len(df['Time']), 80))

fTime = df['Time'][::80]
gTime = []
for i in fTime:
    a = i[:-14]
    gTime.append(a)

plt.xticks(xAx, gTime)
plt.title('Wiimmfi MarioKart', y=1.08)
plt.xlabel('Time')
plt.ylabel('No. of Players Online')
plt.plot(df['Vs. Players'], color='blue')
plt.plot(df['Room Players'], color='red')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
plt.rcParams.update({'font.size': 10})

plt.grid()
plt.show()
