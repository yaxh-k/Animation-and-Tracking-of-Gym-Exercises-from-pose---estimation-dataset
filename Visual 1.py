import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import imageio
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import Axes3D


plt.rcParams['figure.figsize'] = (6,4)
plt.rcParams['figure.dpi'] = 150


df = pd.read_csv("pose-output.csv")




df = df.drop(columns=['right_elbow__right_wrist', 'left_hip__left_ankle', 'right_hip__right_ankle', 'right_wrist__right_shoulder', 'right_knee__left_knee', 'right_ankle__left_ankle', 'right_wrist__right_ankle', 'left_wrist__left_ankle', 'right_wrist__right_knee', 'left_wrist__left_knee','left_shoulder__left_wrist', 'right_wrist__left_wrist', 'left_elbow__left_wrist'])


#we observe that there are 36 columns. 3 coordinates for 12 points: left and right shoulders(2), elbows(2), wrists(2), hips(2), knees(2), ankles(2), 



r = 22 #row number - choose one to display the exercise name and it's visualition
print("The exercise displayed is:", df["name"][r])




#a dataframe containing only the required row
df_visual = df[df["name"] == df["name"][r]]








#convert the strings in columns to lists
for i in range(1, len(list(df_visual.columns))):
  s = df_visual[df_visual.columns[i]][r]
  s = s[1:-2:]    #getting rid of the first and last element of the string
  s = s.split(",")  #converting the string into a list, separating the values by comma
  df_visual[df_visual.columns[i]][r] = s









def line_add(x1, y1, z1, x2, y2, z2):
  l = x2 - x1
  m = y2 - y1
  n = z2 - z1
  xl = np.linspace(x1, x2, num=100)
  yl = (m/l)*(xl - x1) + y1
  zl = (n/l)*(xl - x1) + z1
  return xl, yl, zl








for i in range(len(df_visual['xX_right_hip'][r])):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')







    #PLOTS
    


    #elbows
    ax.scatter(float(df_visual["xX_right_elbow"][r][i]), float(df_visual["zZ_right_elbow"][r][i]), -float(df_visual["yY_right_elbow"][r][i]), c='black')

    ax.scatter(float(df_visual["xX_left_elbow"][r][i]), float(df_visual["zZ_left_elbow"][r][i]), -float(df_visual["yY_left_elbow"][r][i]), c='black')



    #ankle
    ax.scatter(float(df_visual["xX_right_ankle"][r][i]), float(df_visual["zZ_right_ankle"][r][i]), -float(df_visual["yY_right_ankle"][r][i]), c='orange')

    ax.scatter(float(df_visual["xX_left_ankle"][r][i]), float(df_visual["zZ_left_ankle"][r][i]), -float(df_visual["yY_left_ankle"][r][i]), c='orange')

    
    
    #wrists
    ax.scatter(float(df_visual["xX_right_wrist"][r][i]), float(df_visual["zZ_right_wrist"][r][i]), -float(df_visual["yY_right_wrist"][r][i]), c='yellow')

    ax.scatter(float(df_visual["xX_left_wrist"][r][i]), float(df_visual["zZ_left_wrist"][r][i]), -float(df_visual["yY_left_wrist"][r][i]), c='yellow')



    #hip
    ax.scatter(float(df_visual["xX_right_hip"][r][i]), float(df_visual["zZ_right_hip"][r][i]), -float(df_visual["yY_right_hip"][r][i]), c='green')

    ax.scatter(float(df_visual["xX_left_hip"][r][i]), float(df_visual["zZ_left_hip"][r][i]), -float(df_visual["yY_left_hip"][r][i]), c='green')


    #shoulders
    ax.scatter(float(df_visual["xX_right_shoulder"][r][i]), float(df_visual["zZ_right_shoulder"][r][i]), -float(df_visual["yY_right_shoulder"][r][i]), c = 'red')

    ax.scatter(float(df_visual["xX_left_shoulder"][r][i]), float(df_visual["zZ_left_shoulder"][r][i]), -float(df_visual["yY_left_shoulder"][r][i]), c = 'red')


    #knee
    ax.scatter(float(df_visual["xX_right_knee"][r][i]), float(df_visual["zZ_right_knee"][r][i]), -float(df_visual["yY_right_knee"][r][i]), c='blue')

    ax.scatter(float(df_visual["xX_left_knee"][r][i]), float(df_visual["zZ_left_knee"][r][i]), -float(df_visual["yY_left_knee"][r][i]), c='blue')






    #Lines
    #wrist to elbow
    a, b, c = line_add(float(df_visual["xX_right_elbow"][r][i]), float(df_visual["zZ_right_elbow"][r][i]), -float(df_visual["yY_right_elbow"][r][i]), float(df_visual["xX_right_wrist"][r][i]), float(df_visual["zZ_right_wrist"][r][i]), -float(df_visual["yY_right_wrist"][r][i]))
    ax.plot3D(a, b, c, 'red')
    a, b, c = line_add(float(df_visual["xX_left_elbow"][r][i]), float(df_visual["zZ_left_elbow"][r][i]), -float(df_visual["yY_left_elbow"][r][i]), float(df_visual["xX_left_wrist"][r][i]), float(df_visual["zZ_left_wrist"][r][i]), -float(df_visual["yY_left_wrist"][r][i]))
    ax.plot3D(a, b, c, 'red')

    

    #shoulder to shoulder
    a, b, c = line_add(float(df_visual["xX_right_shoulder"][r][i]), float(df_visual["zZ_right_shoulder"][r][i]), -float(df_visual["yY_right_shoulder"][r][i]), float(df_visual["xX_left_shoulder"][r][i]), float(df_visual["zZ_left_shoulder"][r][i]), -float(df_visual["yY_left_shoulder"][r][i]))
    ax.plot3D(a, b, c, 'red')





    #ankle to knee
    a, b, c = line_add(float(df_visual["xX_right_knee"][r][i]), float(df_visual["zZ_right_knee"][r][i]), -float(df_visual["yY_right_knee"][r][i]), float(df_visual["xX_right_ankle"][r][i]), float(df_visual["zZ_right_ankle"][r][i]), -float(df_visual["yY_right_ankle"][r][i]))
    ax.plot3D(a, b, c, 'red')
    a, b, c = line_add(float(df_visual["xX_left_knee"][r][i]), float(df_visual["zZ_left_knee"][r][i]), -float(df_visual["yY_left_knee"][r][i]), float(df_visual["xX_left_ankle"][r][i]), float(df_visual["zZ_left_ankle"][r][i]), -float(df_visual["yY_left_ankle"][r][i]))
    ax.plot3D(a, b, c, 'red')




    #knee to hip
    a, b, c = line_add(float(df_visual["xX_right_knee"][r][i]), float(df_visual["zZ_right_knee"][r][i]), -float(df_visual["yY_right_knee"][r][i]), float(df_visual["xX_right_hip"][r][i]), float(df_visual["zZ_right_hip"][r][i]), -float(df_visual["yY_right_hip"][r][i]))
    ax.plot3D(a, b, c, 'red')
    a, b, c = line_add(float(df_visual["xX_left_knee"][r][i]), float(df_visual["zZ_left_knee"][r][i]), -float(df_visual["yY_left_knee"][r][i]), float(df_visual["xX_left_hip"][r][i]), float(df_visual["zZ_left_hip"][r][i]), -float(df_visual["yY_left_hip"][r][i]))
    ax.plot3D(a, b, c, 'red')




    #left to right hip
    a, b, c = line_add(float(df_visual["xX_right_hip"][r][i]), float(df_visual["zZ_right_hip"][r][i]), -float(df_visual["yY_right_hip"][r][i]), float(df_visual["xX_left_hip"][r][i]), float(df_visual["zZ_left_hip"][r][i]), -float(df_visual["yY_left_hip"][r][i]))
    ax.plot3D(a, b, c, 'red')

    


    #elbow to shoulder
    a, b, c = line_add(float(df_visual["xX_right_elbow"][r][i]), float(df_visual["zZ_right_elbow"][r][i]), -float(df_visual["yY_right_elbow"][r][i]), float(df_visual["xX_right_shoulder"][r][i]), float(df_visual["zZ_right_shoulder"][r][i]), -float(df_visual["yY_right_shoulder"][r][i]))
    ax.plot3D(a, b, c, 'red')
    a, b, c = line_add(float(df_visual["xX_left_elbow"][r][i]), float(df_visual["zZ_left_elbow"][r][i]), -float(df_visual["yY_left_elbow"][r][i]), float(df_visual["xX_left_shoulder"][r][i]), float(df_visual["zZ_left_shoulder"][r][i]), -float(df_visual["yY_left_shoulder"][r][i]))
    ax.plot3D(a, b, c, 'red')







    shoulder_mid_x = (float(df_visual["xX_right_shoulder"][r][i]) + float(df_visual["xX_left_shoulder"][r][i]))/2
    shoulder_mid_y = (float(df_visual["zZ_right_shoulder"][r][i]) + float(df_visual["zZ_left_shoulder"][r][i]))/2
    shoulder_mid_z = -(float(df_visual["yY_right_shoulder"][r][i]) + float(df_visual["yY_left_shoulder"][r][i]))/2





    hip_mid_x = (float(df_visual["xX_right_hip"][r][i]) + float(df_visual["xX_left_hip"][r][i]))/2
    hip_mid_y = (float(df_visual["zZ_right_hip"][r][i]) + float(df_visual["zZ_left_hip"][r][i]))/2
    hip_mid_z = -(float(df_visual["yY_right_hip"][r][i]) + float(df_visual["yY_left_hip"][r][i]))/2




    #hip mid to head
    a, b, c = line_add(hip_mid_x, hip_mid_y, hip_mid_z, shoulder_mid_x + 0.25*(shoulder_mid_x - hip_mid_x), shoulder_mid_y + 0.25*(shoulder_mid_y - hip_mid_y), shoulder_mid_z + 0.25*(shoulder_mid_z - hip_mid_z))
    ax.plot3D(a, b, c, 'red')

    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")
    ax.set_zlabel("Z-Axis")

    plt.savefig(str(i)+'.png')
    plt.close()











a = []

for i in range(len(df_visual['xX_left_hip'][r])):
  a.append(str(i) + '.png')





#Animation GIF
with imageio.get_writer('animate.gif', mode='I') as writer:
    for filename in a:
        image = imageio.imread(filename)
        writer.append_data(image)




