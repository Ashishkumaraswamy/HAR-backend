import numpy as np
import pandas as pd
from scipy import stats
from numpy import linalg as LA

gyscope_val = np.random.uniform(-1,1,384)
gyscope_val = gyscope_val.reshape(128,3)


def bodyandgravity(t_acceleromter,shape1,shape2):
    gx=0 
    gy=0
    gz=0
    body=np.zeros((shape1,shape2))
    gravity=np.zeros((shape1,shape2))
    # print(shape1," ",shape2)
    for i in range(0,shape1):
        gx=0.9*gx+0.1*t_acceleromter[i][0]
        gy=0.9*gx+0.1*t_acceleromter[i][1]
        gz=0.9*gx+0.1*t_acceleromter[i][2]
        body[i][0]=t_acceleromter[i][0]-gx
        body[i][1]=t_acceleromter[i][1]-gy
        body[i][2]=t_acceleromter[i][2]-gy
        gravity[i][0]=gx
        gravity[i][1]=gy
        gravity[i][2]=gz
    return body,gravity

def main(t_accelerometer):
    body,gravity=bodyandgravity(t_accelerometer,t_accelerometer.shape[0],t_accelerometer.shape[1])
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
    # print(len(firstlist))
    # print(len(secondlist))
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

def extract_features(gyroscope,accelerometer):
    f_1,f_3 = main(accelerometer)
    f_2,f_4 = tbodyjerkgro(gyroscope)
    f_1.extend(f_2)
    f_1.extend(f_3)
    f_1.extend(f_4)
    features_cal = f_1
    print(len(features_cal))
    return features_cal

# input_json = {"gyroscope":[[-0.024859048426151276,0.010373157449066639,0.007467169314622879],[-0.05149063840508461,0.010905790142714977,-0.004250729456543922],[-0.044566426426172256,0.012503684498369694,-0.010109677910804749],[-0.029120102524757385,0.020493159070611,-0.00957704707980156],[-0.01953273080289364,0.0077099986374378204,-0.0218275785446167],[-0.0019558833446353674,0.014634213410317898,-0.03674126788973808],[-0.0008906195871531963,0.030080532655119896,-0.011707574129104614],[0.008164120838046074,0.018895264714956284,-0.003185465931892395],[0.015088332816958427,0.04819001629948616,-0.022892840206623077],[0.015088332816958427,0.050853174179792404,-0.04313284903764725],[-0.0040864101611077785,0.05191843584179878,-0.036208637058734894],[-0.015804307535290718,0.027950003743171692,-0.02555599808692932],[-0.014206413179636002,0.0039815763011574745,0.0048040105029940605],[-0.003553778398782015,0.0023836810141801834,-0.005315992049872875],[0.00017464393749833107,-0.0066710589453577995,-0.005315992049872875],[-0.006749568972736597,0.0039815763011574745,-0.015968628227710724],[-0.01473904587328434,-0.0066710589453577995,-0.019164418801665306],[-0.013673782348632812,-0.004540531896054745,-0.01703389175236225],[-0.01473904587328434,0.008775263093411922,-0.00957704707980156],[0.03159991651773453,0.017297370359301567,-0.0005223072366788983],[0.04278518632054329,0.005046839825809002,0.005336642265319824],[-0.012075886130332947,-0.007736322935670614,-0.001054938999004662],[-0.04403379186987877,-0.008801585994660854,0.0016082198126241565],[-0.00142325134947896,-0.20747323334217072,0.006934537552297115],[0.003903066273778677,-0.40880802273750305,0.1102650985121727],[0.00017464393749833107,-0.37152379751205444,0.11079773306846619],[0.01828412525355816,-0.2037448137998581,0.09322088211774826],[0.06622098386287689,-0.12385004758834839,0.030370334163308144],[0.08646099269390106,-0.06259739398956299,-0.030882317572832108],[0.08699362725019455,-0.08230477571487427,-0.03301284462213516],[0.05823150649666786,-0.184037446975708,0.0277071762830019],[-0.024859048426151276,-0.08177213370800018,0.024511385709047318],[0.023077810183167458,0.050853174179792404,-0.03780652955174446],[0.08646099269390106,0.0023836810141801834,-0.05165495350956917],[0.06355782598257065,0.0156994741410017,-0.018631786108016968],[0.010827280580997467,0.010905790142714977,0.02823980711400509],[-0.01047799177467823,-0.0013447412056848407,0.02823980711400509],[-0.00568430544808507,0.013568948023021221,0.012260855175554752],[-0.01846746727824211,0.026352109387516975,0.01492401398718357],[-0.006216937210410833,0.01996052823960781,0.003738746978342533],[-0.025924311950802803,0.010373157449066639,0.007999801076948643],[-0.053088534623384476,0.018895264714956284,0.015456645749509335],[-0.045631688088178635,0.021025793626904488,0.0016082198126241565],[0.006033593323081732,0.02475421503186226,-0.012772835791110992],[0.05237255617976189,0.05298370122909546,-0.018631786108016968],[0.04811150208115578,0.02901526726782322,-0.003185465931892395],[0.024675704538822174,-0.00027947771013714373,0.007467169314622879],[-0.02326115220785141,0.00025315405218861997,-0.014370733872056007],[-0.029120102524757385,-0.00027947771013714373,-0.028219159692525864],[0.024143071845173836,0.025819478556513786,-0.0026528341695666313],[0.06835151463747025,0.029547901824116707,0.020250331610441208],[0.03905675932765007,0.008242630399763584,0.021848227828741074],[0.009229382500052452,-0.030639488250017166,0.0032061152160167694],[0.03532833978533745,-0.018921589478850365,-0.007446520030498505],[0.049176763743162155,0.02422158233821392,-0.007446520030498505],[0.11362520605325699,0.02368895150721073,0.0032061152160167694],[0.15303994715213776,0.06257106363773346,-0.014370733872056007],[0.13919152319431305,0.07215844094753265,-0.04153495281934738],[0.040654655545949936,0.03540685027837753,-0.03514336794614792],[-0.05255590006709099,-0.0018773729680106044,-0.020229680463671684],[-0.03657694533467293,0.00984052661806345,-0.035676002502441406],[0.033197809010744095,0.02901526726782322,-0.036208637058734894],[0.05024202540516853,0.03167843073606491,-0.02236020937561989],[-0.014206413179636002,-0.014127903617918491,-0.0026528341695666313]],"accelerometer":[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]}
# data= extract_features(np.array(input_json['gyroscope']),np.array(input_json['accelerometer']))
# print(len(data))