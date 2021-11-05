import numpy as np
import pandas as pd
from scipy import stats
from numpy import linalg as LA
np.seterr(divide='ignore', invalid='ignore')
from sklearn.preprocessing import MinMaxScaler

def bodyandgravity(t_acceleromter,shape1,shape2):
    gx=0 
    gy=0
    gz=0
    body=np.zeros((shape1,shape2))
    gravity=np.zeros((shape1,shape2))
    # print(shape1," ",shape2)
    for i in range(0,shape1):
        gx=0.8*gx+0.2*t_acceleromter[i][0]
        gy=0.8*gy+0.2*t_acceleromter[i][1]
        gz=0.8*gz+0.2*t_acceleromter[i][2]
        body[i][0]=t_acceleromter[i][0]-gx
        body[i][1]=t_acceleromter[i][1]-gy
        body[i][2]=t_acceleromter[i][2]-gz
        gravity[i][0]=gx
        gravity[i][1]=gy
        gravity[i][2]=gz
    return body,gravity

# def sepbodygravity(t_accelerometer):
#     shape1=t_accelerometer.shape[0]
#     shape2=t_accelerometer.shape[1]
#     body=np.zeros((shape1,shape2))
#     gravity=np.zeros((shape1,shape2))
#     fs=50
#     nyq=0.5*fs
#     cutoff= 0.35
#     normal_cutoff=cutoff/nyq
#     order=1
#     timeStep=1/fs
#     b,a=butter(order,normal_cutoff,btype='low',analog=True)
#     gravity[:,0]=lfilter(b,a,t_accelerometer[:,0])
#     gravity[:,1]=lfilter(b,a,t_accelerometer[:,1])
#     gravity[:,2]=lfilter(b,a,t_accelerometer[:,2])
#     body[:,0]=t_accelerometer[:,0]-gravity[:,0]
#     body[:,1]=t_accelerometer[:,1]-gravity[:,1]
#     body[:,2]=t_accelerometer[:,2]-gravity[:,2]
#     return body,gravity

def main(body,gravity):
    # body=t_accelerometer
    # gravity=gaccelerometer
    firstlist=[]
    secondlist=[]
    #1
    tbodyaccmeanx=np.mean(body[:,0])
    firstlist.append(tbodyaccmeanx)
    #2
    tbodyaccmeany=np.mean(body[:,1])
    firstlist.append(tbodyaccmeany)
    #3
    tbodyaccmeanz=np.mean(body[:,2])
    firstlist.append(tbodyaccmeanz)
    #4
    tbodyaccstdx=np.std(body[:,0])
    firstlist.append(tbodyaccstdx)
    #5
    tbodyaccstdy=np.std(body[:,1])
    firstlist.append(tbodyaccstdy)
    #6
    tbodyaccstdz=np.std(body[:,2])
    firstlist.append(tbodyaccstdz)
    #7
    tbodyaccmadx=np.mean(np.absolute(body[:,0]-np.mean(body[:,0])))
    firstlist.append(tbodyaccmadx)
    # print(tbodyaccmadx)
    #8
    tbodyaccmady=np.mean(np.absolute(body[:,1]-np.mean(body[:,1])))
    firstlist.append(tbodyaccmady)
    #9
    tbodyaccmadz=np.mean(np.absolute(body[:,2]-np.mean(body[:,2])))
    firstlist.append(tbodyaccmadz)
    #10
    tbodymaxx=np.max(body[:,0])
    firstlist.append(tbodymaxx)
    #11
    tbodymaxy=np.max(body[:,1])
    firstlist.append(tbodymaxy)
    #12
    tbodymaxz=np.max(body[:,2])
    firstlist.append(tbodymaxz)
    #13
    tbodyminx=np.min(body[:,0])
    firstlist.append(tbodyminx)
    #14
    tbodyminy=np.min(body[:,1])
    firstlist.append(tbodyminy)
    #15
    tbodyminz=np.min(body[:,2])
    firstlist.append(tbodyminz)
    #16
    tbodyacciqrx=stats.iqr(body[:,0],interpolation="midpoint")
    firstlist.append(tbodyacciqrx)
    # print(tbodyacciqrx)
    #17
    tbodyacciqry=stats.iqr(body[:,1],interpolation="midpoint")
    firstlist.append(tbodyacciqry)
    #18
    tbodyacciqrz=stats.iqr(body[:,2],interpolation="midpoint")
    firstlist.append(tbodyacciqrz)
    #19
    tbodycorrxy=np.corrcoef(body[:,0],body[:,1])
    firstlist.append(tbodycorrxy[0 , 1])
    #20
    tbodycorrxz=np.corrcoef(body[:,0],body[:,2])
    firstlist.append(tbodycorrxz[0 , 1])
    #21
    tbodycorryz=np.corrcoef(body[:,1],body[:,2])
    firstlist.append(tbodycorryz[0 , 1])
    #22
    tgravitymeanx=np.mean(gravity[:,0])
    firstlist.append(tgravitymeanx)
    #23
    tgravitymeany=np.mean(gravity[:,1])
    firstlist.append(tgravitymeany)
    #24
    tgravitymeanz=np.mean(gravity[:,2])
    firstlist.append(tgravitymeanz)
    #25
    tgravitystdx=np.std(gravity[:,0])
    firstlist.append(tgravitystdx)
    #26
    tgravitystdy=np.std(gravity[:,1])
    firstlist.append(tgravitystdy)
    #27
    tgravitystdz=np.std(gravity[:,2])
    firstlist.append(tgravitystdz)
    #28
    tgravitymadx=np.mean(np.absolute(gravity[:,0]-np.mean(gravity[:,0])))
    firstlist.append(tgravitymadx)
    #29
    tgravitymady=np.mean(np.absolute(gravity[:,1]-np.mean(gravity[:,1])))
    firstlist.append(tgravitymady)
    #30
    tgravitymadz=np.mean(np.absolute(gravity[:,2]-np.mean(gravity[:,2])))
    firstlist.append(tgravitymadz)
    #31
    tgravitymaxx=np.max(gravity[:,0])
    firstlist.append(tgravitymaxx)
    #32
    tgravitymaxy=np.max(gravity[:,1])
    firstlist.append(tgravitymaxy)
    #33
    tgravitymaxz=np.max(gravity[:,2])
    firstlist.append(tgravitymaxz)
    #34
    tgravityminx=np.min(gravity[:,0])
    firstlist.append(tgravityminx)
    #35
    tgravityminy=np.min(gravity[:,1])
    firstlist.append(tgravityminy)
    #36
    tgravityminz=np.min(gravity[:,2])
    firstlist.append(tgravityminz)
    #37
    tgravityacciqrx=stats.iqr(gravity[:,0],interpolation="midpoint")
    firstlist.append(tgravityacciqrx)
    # print(tgravityacciqrx)
    #38
    tgravityacciqry=stats.iqr(gravity[:,1],interpolation="midpoint")
    firstlist.append(tgravityacciqry)
    #39
    tgravityacciqrz=stats.iqr(gravity[:,2],interpolation="midpoint")
    firstlist.append(tgravityacciqrz)
    #40
    tgravitycorrxy=np.corrcoef(gravity[:,0],gravity[:,1])
    firstlist.append(tgravitycorrxy[0 , 1])
    #41
    tgravitycorrxz=np.corrcoef(gravity[:,0],gravity[:,2])
    firstlist.append(tgravitycorrxz[0 , 1])
    #42
    tgravitycorryz=np.corrcoef(gravity[:,1],gravity[:,2])
    firstlist.append(tgravitycorryz[0 , 1])
    #64
    tbodyaccmagmean=np.mean(LA.norm(body,axis=1))
    secondlist.append(tbodyaccmagmean)
    #65
    tbodyaccmagstd=np.std(LA.norm(body,axis=1))
    secondlist.append(tbodyaccmagstd)
    #66
    norm=LA.norm(body,axis=1)
    tbodyaccmagmad=np.mean(np.absolute(norm-np.mean(norm)))
    secondlist.append(tbodyaccmagmad)
    #67
    tbodyaccmagmaxx=np.max(LA.norm(body,axis=1))
    secondlist.append(tbodyaccmagmaxx)
    #68
    tbodyaccmagminx=np.min(LA.norm(body,axis=1))
    secondlist.append(tbodyaccmagminx)
    #69
    norm=LA.norm(body,axis=1)
    tbodyaccmagiqr=stats.iqr(norm,interpolation="midpoint")
    secondlist.append(tbodyaccmagiqr)
    #70
    tgravityaccmagmean=np.mean(LA.norm(gravity,axis=1))
    secondlist.append(tgravityaccmagmean)
    #71
    tgravityaccmagstd=np.std(LA.norm(gravity,axis=1))
    secondlist.append(tgravityaccmagstd)
    #72
    norm=LA.norm(gravity,axis=1)
    tgravityaccmagmad=np.mean(np.absolute(norm-np.mean(norm)))
    secondlist.append(tgravityaccmagmad)
    # print(tgravityaccmagmad)
    #73
    tgravityaccmagmaxx=np.max(LA.norm(gravity,axis=1))
    secondlist.append(tgravityaccmagmaxx)
    #74
    tgravityaccmagminx=np.min(LA.norm(gravity,axis=1))
    secondlist.append(tgravityaccmagminx)
    #75
    norm=LA.norm(gravity,axis=1)
    tgravityaccmagiqr=stats.iqr(norm,interpolation="midpoint")
    secondlist.append(tgravityaccmagiqr)
    # # print(len(firstlist))
    # # print(len(secondlist))
    return firstlist,secondlist


def tbodyjerkgro(gyscope_val):
    gyro_list = []
    gyro_list_2 = []
    column_means = gyscope_val.mean(axis=0)
    #43
    tBodyGyro_mean_X = column_means[0]
    gyro_list.append(tBodyGyro_mean_X)
    #44
    tBodyGyro_mean_y = column_means[1]
    gyro_list.append(tBodyGyro_mean_y)
    #45
    tBodyGyro_mean_Z = column_means[2]
    gyro_list.append(tBodyGyro_mean_Z)
    
    x = gyscope_val[:,[0]].reshape(1,gyscope_val.shape[0])
    y = gyscope_val[:,[1]].reshape(1,gyscope_val.shape[0])
    z = gyscope_val[:,[2]].reshape(1,gyscope_val.shape[0])
    x = x[0]
    y = y[0]
    z = z[0]
    #46
    tBodyGyro_std_X = np.std(x)
    gyro_list.append(tBodyGyro_std_X)
    #47
    tBodyGyro_std_y = np.std(y)
    gyro_list.append(tBodyGyro_std_y)
    #48
    tBodyGyro_std_z = np.std(z)
    gyro_list.append(tBodyGyro_std_z)
    #49
    tBodyGyro_mad_X = np.mean(np.absolute(x - np.mean(x)))
    gyro_list.append(tBodyGyro_mad_X)
    #50
    tBodyGyro_mad_y = np.mean(np.absolute(y - np.mean(y)))
    gyro_list.append(tBodyGyro_mad_y)
    #51
    tBodyGyro_mad_z = np.mean(np.absolute(z - np.mean(z)))
    gyro_list.append(tBodyGyro_mad_z)
    #52
    gyro_list.append(np.max(x))
    #53
    gyro_list.append(np.max(y))
    #54
    gyro_list.append(np.max(z))
    #55
    gyro_list.append(np.min(x))
    #56
    gyro_list.append(np.min(y))
    #57
    gyro_list.append(np.min(z))
    #58
    gyro_list.append(stats.iqr(x, interpolation = 'midpoint'))
    #59
    gyro_list.append(stats.iqr(y, interpolation = 'midpoint'))
    #60
    gyro_list.append(stats.iqr(z, interpolation = 'midpoint'))
    tBodyGyro_correlation_X_Y = np.corrcoef(x, y)
    tBodyGyro_correlation_X_Z = np.corrcoef(x, z)
    tBodyGyro_correlation_Y_Z = np.corrcoef(y, z)

    tBodyGyro_correlation_X_Y = tBodyGyro_correlation_X_Y[0 , 1]
    #61
    gyro_list.append(tBodyGyro_correlation_X_Y)

    tBodyGyro_correlation_X_Z = tBodyGyro_correlation_X_Z[0 , 1]
    #62
    gyro_list.append(tBodyGyro_correlation_X_Z)

    tBodyGyro_correlation_Y_Z = tBodyGyro_correlation_Y_Z[0 , 1]
    #63
    gyro_list.append(tBodyGyro_correlation_Y_Z)

    tBodyGyroMag = LA.norm(gyscope_val, axis=1)
    #76
    gyro_list_2.append(np.mean(tBodyGyroMag))
    #77
    gyro_list_2.append(np.std(tBodyGyroMag))
    #78
    gyro_list_2.append(np.mean(np.absolute(tBodyGyroMag - np.mean(tBodyGyroMag))))
    #79
    gyro_list_2.append(np.max(tBodyGyroMag))
    #80
    gyro_list_2.append(np.min(tBodyGyroMag))
    #81
    gyro_list_2.append(stats.iqr(tBodyGyroMag, interpolation = 'midpoint'))
    
    return gyro_list,gyro_list_2

def extract_features(gyroscope,lin_accelerometer,grav_acceleromter):
    f_1,f_3 = main(lin_accelerometer,grav_acceleromter)
    f_2,f_4 = tbodyjerkgro(gyroscope)
    f_1.extend(f_2)
    f_1.extend(f_3)
    f_1.extend(f_4)
    features_cal = f_1
    return features_cal

# input_json = {"gyroscope":[[0.0010689827613532543,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[0.0010689827613532543,-0.0021379655227065086,-0.00015271181473508477],[0.0022906772792339325,-0.0009162708884105086,-0.00015271181473508477],[-0.00259610079228878,0.0015271181473508477,-0.00015271181473508477],[-0.00015271181473508477,-0.0021379655227065086,-0.00015271181473508477],[0.0010689827613532543,-0.0021379655227065086,-0.00015271181473508477],[-0.00015271181473508477,-0.0021379655227065086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.0015271181473508477,-0.00015271181473508477],[-0.001374406274408102,0.0015271181473508477,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[0.0022906772792339325,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.004581354558467865,-0.00015271181473508477],[0.0022906772792339325,-0.007024743594229221,-0.00015271181473508477],[0.0022906772792339325,-0.0021379655227065086,-0.00015271181473508477],[-0.00015271181473508477,0.0015271181473508477,-0.001374406274408102],[-0.001374406274408102,0.002748812548816204,0.0010689827613532543],[-0.00015271181473508477,0.0015271181473508477,-0.00015271181473508477],[-0.00015271181473508477,0.0015271181473508477,-0.00015271181473508477],[-0.001374406274408102,0.0015271181473508477,0.0010689827613532543],[0.0010689827613532543,0.00030542362947016954,0.0010689827613532543],[-0.001374406274408102,0.00030542362947016954,0.0010689827613532543],[-0.00015271181473508477,-0.0009162708884105086,-0.00259610079228878],[0.0022906772792339325,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.001374406274408102],[0.0022906772792339325,-0.0021379655227065086,-0.00015271181473508477],[-0.001374406274408102,0.0015271181473508477,-0.00015271181473508477],[-0.00259610079228878,0.00519220158457756,-0.001374406274408102],[-0.001374406274408102,0.0015271181473508477,-0.001374406274408102],[0.0022906772792339325,-0.0009162708884105086,0.0010689827613532543],[0.0010689827613532543,-0.0021379655227065086,-0.00015271181473508477],[-0.00015271181473508477,0.0015271181473508477,0.0010689827613532543],[-0.00015271181473508477,0.0015271181473508477,-0.00015271181473508477],[-0.001374406274408102,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0021379655227065086,-0.00015271181473508477],[-0.001374406274408102,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.002748812548816204,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.003359660040587187,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.001374406274408102,-0.0009162708884105086,0.0010689827613532543],[-0.001374406274408102,-0.0009162708884105086,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,0.0015271181473508477,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.001374406274408102],[0.0010689827613532543,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.0015271181473508477,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0021379655227065086,-0.001374406274408102],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.001374406274408102,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[-0.001374406274408102,-0.0009162708884105086,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.001374406274408102,0.00030542362947016954,-0.001374406274408102],[-0.001374406274408102,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[-0.001374406274408102,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.010078979656100273,-0.00015271181473508477],[-0.001374406274408102,0.00519220158457756,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.004581354558467865,0.0010689827613532543],[0.0010689827613532543,-0.003359660040587187,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477]],"accelerometer":[[0.0010689827613532543,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[0.0010689827613532543,-0.0021379655227065086,-0.00015271181473508477],[0.0022906772792339325,-0.0009162708884105086,-0.00015271181473508477],[-0.00259610079228878,0.0015271181473508477,-0.00015271181473508477],[-0.00015271181473508477,-0.0021379655227065086,-0.00015271181473508477],[0.0010689827613532543,-0.0021379655227065086,-0.00015271181473508477],[-0.00015271181473508477,-0.0021379655227065086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.0015271181473508477,-0.00015271181473508477],[-0.001374406274408102,0.0015271181473508477,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[0.0022906772792339325,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.004581354558467865,-0.00015271181473508477],[0.0022906772792339325,-0.007024743594229221,-0.00015271181473508477],[0.0022906772792339325,-0.0021379655227065086,-0.00015271181473508477],[-0.00015271181473508477,0.0015271181473508477,-0.001374406274408102],[-0.001374406274408102,0.002748812548816204,0.0010689827613532543],[-0.00015271181473508477,0.0015271181473508477,-0.00015271181473508477],[-0.00015271181473508477,0.0015271181473508477,-0.00015271181473508477],[-0.001374406274408102,0.0015271181473508477,0.0010689827613532543],[0.0010689827613532543,0.00030542362947016954,0.0010689827613532543],[-0.001374406274408102,0.00030542362947016954,0.0010689827613532543],[-0.00015271181473508477,-0.0009162708884105086,-0.00259610079228878],[0.0022906772792339325,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.001374406274408102],[0.0022906772792339325,-0.0021379655227065086,-0.00015271181473508477],[-0.001374406274408102,0.0015271181473508477,-0.00015271181473508477],[-0.00259610079228878,0.00519220158457756,-0.001374406274408102],[-0.001374406274408102,0.0015271181473508477,-0.001374406274408102],[0.0022906772792339325,-0.0009162708884105086,0.0010689827613532543],[0.0010689827613532543,-0.0021379655227065086,-0.00015271181473508477],[-0.00015271181473508477,0.0015271181473508477,0.0010689827613532543],[-0.00015271181473508477,0.0015271181473508477,-0.00015271181473508477],[-0.001374406274408102,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0021379655227065086,-0.00015271181473508477],[-0.001374406274408102,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.002748812548816204,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.003359660040587187,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.001374406274408102,-0.0009162708884105086,0.0010689827613532543],[-0.001374406274408102,-0.0009162708884105086,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,0.0015271181473508477,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.001374406274408102],[0.0010689827613532543,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.0015271181473508477,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0021379655227065086,-0.001374406274408102],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.001374406274408102,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[-0.001374406274408102,-0.0009162708884105086,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.001374406274408102,0.00030542362947016954,-0.001374406274408102],[-0.001374406274408102,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[-0.001374406274408102,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.010078979656100273,-0.00015271181473508477],[-0.001374406274408102,0.00519220158457756,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.004581354558467865,0.0010689827613532543],[0.0010689827613532543,-0.003359660040587187,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477]],"accelerometer_gravity":[[0.0010689827613532543,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[0.0010689827613532543,-0.0021379655227065086,-0.00015271181473508477],[0.0022906772792339325,-0.0009162708884105086,-0.00015271181473508477],[-0.00259610079228878,0.0015271181473508477,-0.00015271181473508477],[-0.00015271181473508477,-0.0021379655227065086,-0.00015271181473508477],[0.0010689827613532543,-0.0021379655227065086,-0.00015271181473508477],[-0.00015271181473508477,-0.0021379655227065086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.0015271181473508477,-0.00015271181473508477],[-0.001374406274408102,0.0015271181473508477,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[0.0022906772792339325,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.004581354558467865,-0.00015271181473508477],[0.0022906772792339325,-0.007024743594229221,-0.00015271181473508477],[0.0022906772792339325,-0.0021379655227065086,-0.00015271181473508477],[-0.00015271181473508477,0.0015271181473508477,-0.001374406274408102],[-0.001374406274408102,0.002748812548816204,0.0010689827613532543],[-0.00015271181473508477,0.0015271181473508477,-0.00015271181473508477],[-0.00015271181473508477,0.0015271181473508477,-0.00015271181473508477],[-0.001374406274408102,0.0015271181473508477,0.0010689827613532543],[0.0010689827613532543,0.00030542362947016954,0.0010689827613532543],[-0.001374406274408102,0.00030542362947016954,0.0010689827613532543],[-0.00015271181473508477,-0.0009162708884105086,-0.00259610079228878],[0.0022906772792339325,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.001374406274408102],[0.0022906772792339325,-0.0021379655227065086,-0.00015271181473508477],[-0.001374406274408102,0.0015271181473508477,-0.00015271181473508477],[-0.00259610079228878,0.00519220158457756,-0.001374406274408102],[-0.001374406274408102,0.0015271181473508477,-0.001374406274408102],[0.0022906772792339325,-0.0009162708884105086,0.0010689827613532543],[0.0010689827613532543,-0.0021379655227065086,-0.00015271181473508477],[-0.00015271181473508477,0.0015271181473508477,0.0010689827613532543],[-0.00015271181473508477,0.0015271181473508477,-0.00015271181473508477],[-0.001374406274408102,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0021379655227065086,-0.00015271181473508477],[-0.001374406274408102,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.002748812548816204,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.003359660040587187,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.001374406274408102,-0.0009162708884105086,0.0010689827613532543],[-0.001374406274408102,-0.0009162708884105086,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,0.0015271181473508477,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.001374406274408102],[0.0010689827613532543,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.0015271181473508477,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0021379655227065086,-0.001374406274408102],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.001374406274408102,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[-0.001374406274408102,-0.0009162708884105086,0.0010689827613532543],[-0.00015271181473508477,0.00030542362947016954,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,0.0010689827613532543],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.001374406274408102,0.00030542362947016954,-0.001374406274408102],[-0.001374406274408102,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[0.0010689827613532543,0.00030542362947016954,-0.00015271181473508477],[-0.001374406274408102,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.001374406274408102],[-0.00015271181473508477,0.010078979656100273,-0.00015271181473508477],[-0.001374406274408102,0.00519220158457756,-0.00015271181473508477],[-0.00015271181473508477,-0.0009162708884105086,-0.00015271181473508477],[-0.00015271181473508477,-0.004581354558467865,0.0010689827613532543],[0.0010689827613532543,-0.003359660040587187,-0.001374406274408102],[-0.00015271181473508477,0.00030542362947016954,-0.00015271181473508477]]}
# accelerometer_gravity=input_json['accelerometer_gravity']
# accelerometer=input_json['accelerometer']
# gyroscope=input_json['gyroscope']
# gyroscope=np.array(gyroscope)
# accelerometer=np.array(accelerometer)
# accelerometer_gravity=np.array(accelerometer_gravity)
# gyroscope.reshape(100,3)
# accelerometer.reshape(100,3)
# accelerometer_gravity.reshape(100,3)
# body = np.subtract(accelerometer,accelerometer_gravity)
# scaler=MinMaxScaler(feature_range=(-1,1))
# accelerometer_gravity=scaler.fit_transform(accelerometer_gravity)
# body=scaler.fit_transform(body)
# gyroscope=scaler.fit_transform(gyroscope)
# temp = np.hstack((body,accelerometer_gravity,gyroscope))
# arr=np.mean(temp,axis=0)
# # shape = list(np.array(input_json['gyroscope']).shape)
# # print(data)
# import pickle
# loaded_model = pickle.load(open('rdclfmodel.pkl', 'rb'))
# outputlabel=['LAYING','SITTING','STANDING','WALKING','WALKING_DOWNSTAIRS','WALKING_UPSTAIRS']
# # data = np.array(data)
# pred = loaded_model.predict(arr.reshape(1,9))
# print(pred)

def concat(data):
    
    # Select left pocket data
    
    #Square root of sum of squares of accelerometer, linear acceleration and gyroscope data
    data["MA"] = np.sqrt(np.square(data['Ax']) + np.square(data['Ay']) + np.square(data['Az']))
    data["ML"] = np.sqrt(np.square(data['Lx']) + np.square(data['Ly']) + np.square(data['Lz']))
    data["MG"] = np.sqrt(np.square(data['Gx']) + np.square(data['Gy']) + np.square(data['Gz']))
   
    return data

def generate_sequence(x,n_time_steps, step):
    
    segments = []
    i = 0
    ax = x['Ax'].values[i: i + n_time_steps]
    ay = x['Ay'].values[i: i + n_time_steps]
    az = x['Az'].values[i: i + n_time_steps]

    lx = x['Lx'].values[i: i + n_time_steps]
    ly = x['Ly'].values[i: i + n_time_steps]
    lz = x['Lz'].values[i: i + n_time_steps]
    
    gx = x['Gx'].values[i: i + n_time_steps]
    gy = x['Gy'].values[i: i + n_time_steps]
    gz = x['Gz'].values[i: i + n_time_steps]

    MA = x['MA'].values[i: i + n_time_steps]
    ML = x['ML'].values[i: i + n_time_steps]
    MG = x['MG'].values[i: i + n_time_steps]
    
    segments.append([ax, ay, az, lx, ly, lz, gx, gy, gz, MA, ML, MG])
    
    return segments

def reshape_segments(x, n_time_steps, n_features):
    x_reshaped = np.asarray(x, dtype= np.float32).reshape(-1, n_time_steps, n_features)
    return x_reshaped

# from tensorflow import keras

# N_TIME_STEPS = 100 #sliding window length
# STEP = 50 #Sliding window step size
# N_FEATURES = 12 
# gyroscope=np.array(request['gyroscope'])
# accelerometer=np.array(request['accelerometer'])
# accelerometer_gravity=np.array(request['accelerometer_gravity'])
# gyroscope.reshape(100,3)
# accelerometer.reshape(100,3)
# accelerometer_gravity.reshape(100,3)
# body=np.subtract(accelerometer,accelerometer_gravity)
# li=[accelerometer_gravity,body,gyroscope]
# temp = np.hstack((accelerometer_gravity,body,gyroscope))
# df = pd.DataFrame(temp ,columns=['Ax','Ay','Az','Lx','Ly','Lz','Gx','Gy','Gz'] )
# data = df
# test_X=concat(data)

# test_X=generate_sequence(test_X,N_TIME_STEPS, STEP)
# X_test=reshape_segments(test_X,N_TIME_STEPS, N_FEATURES)
# model=keras.models.load_model('keras_model.h5')
# pred=model.predict(X_test)
# result = output_list[np.argmax(pred)]
# print(result)