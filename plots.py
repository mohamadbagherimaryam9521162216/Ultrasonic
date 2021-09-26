import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import arabic_reshaper
from matplotlib.pyplot import *
from bidi.algorithm import get_display
from pykalman import KalmanFilter

kf = KalmanFilter(transition_matrices = [[1, 1], [0, 1]], observation_matrices = [[0.1, 0.5], [-0.3, 0.0]])
def _(text):
    return get_display(
        arabic_reshaper.reshape(
        u'%s' % str(text)
                                               )
    )

data1= pd.read_csv("data01.csv")
data2=pd.read_csv("data02.csv")
data3=pd.read_csv("data03.csv")
data4=pd.read_csv("data04.csv")

fig = plt.figure()
fig.add_subplot(211, projection='polar')
x1=data1['Measured_dis']
y1=data1['Real_dis']
z1=data1['angle']
e1=data1['error']
z1=(z1*np.pi*2)/360



plt.title(_("01-مربع-35-چرم"), va='bottom')
plt.plot(z1, x1,color="blue",label=_("ثبت شده"))
plt.plot(z1,y1,color="red",label=_("واقعی"))


fig.add_subplot(221, projection='polar')
x2=data2['Measured_dis']
y2=data2['Real_dis']
z2=data2['angle']
e2=data2['error']
z2=(z2*np.pi*2)/360
plt.title(_("02-مستطیل -52-34-پارچه"), va='bottom')
plt.plot(z2, x2,color="blue",label=_("ثبت شده"))
plt.plot(z2,y2,color="red",label=_("واقعی"))

fig.add_subplot(212, projection='polar')
x3=data3['Measured_dis']
y3=data3['Real_dis']
z3=data3['angle']
e3=data3['error']
z3=(z3*np.pi*2)/360
plt.title(_("03-پنج ضلعی-35-چرم"), va='bottom')
plt.plot(z3, x3,color="blue",label=_("ثبت شده"))
plt.plot(z3,y3,color="red",label=_("واقعی"))


fig.add_subplot(223, projection='polar')
x4=data4['Measured_dis']
y4=data4['Real_dis']
z4=data4['angle']
e4=data4['error']
z4=(z4*np.pi*2)/360
plt.title(_("04-ذوزنقه-50-47-80-پارچه"), va='bottom')
plt.plot(z4, x4,color="blue",label=_("ثبت شده"))
plt.plot(z4,y4,color="red",label=_("واقعی"))

plt.legend(bbox_to_anchor=(1.9, 1.8), borderaxespad=0.5)

#ax.set_rmax(2)
#ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
#ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
plt.grid(True)
plt.subplots_adjust(left=0,
                    bottom=0.1,
                    right=1.4,
                    top=0.85,
                    wspace=0.8,
                    hspace=0.6)


plt.show()
