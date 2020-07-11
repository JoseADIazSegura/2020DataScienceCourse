import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../dataSrc/9.1 lsd_math_score_data.csv.csv")
time = data['Time_Delay_in_Minutes']
LSD = data['LSD_ppm']
score = data['Avg_Math_Test_Score']

plt.title('Tissue concentration of LSD over time',fontsize=17)
plt.xlabel('Time in Minutes',fontsize=14)
plt.ylabel('Tissue LSD ppm',fontsize=14)
plt.text(x=0,y=-0.5,s="Wagner et al. (1968)",fontsize=12)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlim(0,500)
plt.ylim(1,7)

plt.style.use('classic')
plt.plot(time,LSD, color='#e74c3c',linewidth=3)
plt.show()