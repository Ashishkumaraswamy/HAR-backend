import numpy as np
import pandas as pd
from scipy import stats
from numpy import linalg as LA
from scipy.signal import butter, lfilter, freqz
np.seterr(divide='ignore', invalid='ignore')
# gyscope_val = np.random.uniform(-1,1,384)
# gyscope_val = gyscope_val.reshape(128,3)


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

def main(t_accelerometer):
    # body=t_accelerometer
    # gravity=gaccelerometer
    body,gravity=bodyandgravity(t_accelerometer,t_accelerometer.shape[0],t_accelerometer.shape[1])
    body=body
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
    # #4
    # tbodyaccstdx=np.std(body[:,0])
    # firstlist.append(tbodyaccstdx)
    # #5
    # tbodyaccstdy=np.std(body[:,1])
    # firstlist.append(tbodyaccstdy)
    # #6
    # tbodyaccstdz=np.std(body[:,2])
    # firstlist.append(tbodyaccstdz)
    # #7
    # tbodyaccmadx=np.mean(np.absolute(body[:,0]-np.mean(body[:,0])))
    # firstlist.append(tbodyaccmadx)
    # # print(tbodyaccmadx)
    # #8
    # tbodyaccmady=np.mean(np.absolute(body[:,1]-np.mean(body[:,1])))
    # firstlist.append(tbodyaccmady)
    # #9
    # tbodyaccmadz=np.mean(np.absolute(body[:,2]-np.mean(body[:,2])))
    # firstlist.append(tbodyaccmadz)
    # #10
    # tbodymaxx=np.max(body[:,0])
    # firstlist.append(tbodymaxx)
    # #11
    # tbodymaxy=np.max(body[:,1])
    # firstlist.append(tbodymaxy)
    # #12
    # tbodymaxz=np.max(body[:,2])
    # firstlist.append(tbodymaxz)
    # #13
    # tbodyminx=np.min(body[:,0])
    # firstlist.append(tbodyminx)
    # #14
    # tbodyminy=np.min(body[:,1])
    # firstlist.append(tbodyminy)
    # #15
    # tbodyminz=np.min(body[:,2])
    # firstlist.append(tbodyminz)
    # #16
    # tbodyacciqrx=stats.iqr(body[:,0],interpolation="midpoint")
    # firstlist.append(tbodyacciqrx)
    # # print(tbodyacciqrx)
    # #17
    # tbodyacciqry=stats.iqr(body[:,1],interpolation="midpoint")
    # firstlist.append(tbodyacciqry)
    # #18
    # tbodyacciqrz=stats.iqr(body[:,2],interpolation="midpoint")
    # firstlist.append(tbodyacciqrz)
    # #19
    # tbodycorrxy=np.corrcoef(body[:,0],body[:,1])
    # firstlist.append(tbodycorrxy[0 , 1])
    # #20
    # tbodycorrxz=np.corrcoef(body[:,0],body[:,2])
    # firstlist.append(tbodycorrxz[0 , 1])
    # #21
    # tbodycorryz=np.corrcoef(body[:,1],body[:,2])
    # firstlist.append(tbodycorryz[0 , 1])
    # #22
    tgravitymeanx=np.mean(gravity[:,0])
    firstlist.append(tgravitymeanx)
    #23
    tgravitymeany=np.mean(gravity[:,1])
    firstlist.append(tgravitymeany)
    #24
    tgravitymeanz=np.mean(gravity[:,2])
    firstlist.append(tgravitymeanz)
    # #25
    # tgravitystdx=np.std(gravity[:,0])
    # firstlist.append(tgravitystdx)
    # #26
    # tgravitystdy=np.std(gravity[:,1])
    # firstlist.append(tgravitystdy)
    # #27
    # tgravitystdz=np.std(gravity[:,2])
    # firstlist.append(tgravitystdz)
    # #28
    # tgravitymadx=np.mean(np.absolute(gravity[:,0]-np.mean(gravity[:,0])))
    # firstlist.append(tgravitymadx)
    # #29
    # tgravitymady=np.mean(np.absolute(gravity[:,1]-np.mean(gravity[:,1])))
    # firstlist.append(tgravitymady)
    # #30
    # tgravitymadz=np.mean(np.absolute(gravity[:,2]-np.mean(gravity[:,2])))
    # firstlist.append(tgravitymadz)
    # #31
    # tgravitymaxx=np.max(gravity[:,0])
    # firstlist.append(tgravitymaxx)
    # #32
    # tgravitymaxy=np.max(gravity[:,1])
    # firstlist.append(tgravitymaxy)
    # #33
    # tgravitymaxz=np.max(gravity[:,2])
    # firstlist.append(tgravitymaxz)
    # #34
    # tgravityminx=np.min(gravity[:,0])
    # firstlist.append(tgravityminx)
    # #35
    # tgravityminy=np.min(gravity[:,1])
    # firstlist.append(tgravityminy)
    # #36
    # tgravityminz=np.min(gravity[:,2])
    # firstlist.append(tgravityminz)
    # #37
    # tgravityacciqrx=stats.iqr(gravity[:,0],interpolation="midpoint")
    # firstlist.append(tgravityacciqrx)
    # # print(tgravityacciqrx)
    # #38
    # tgravityacciqry=stats.iqr(gravity[:,1],interpolation="midpoint")
    # firstlist.append(tgravityacciqry)
    # #39
    # tgravityacciqrz=stats.iqr(gravity[:,2],interpolation="midpoint")
    # firstlist.append(tgravityacciqrz)
    # #40
    # tgravitycorrxy=np.corrcoef(gravity[:,0],gravity[:,1])
    # firstlist.append(tgravitycorrxy[0 , 1])
    # #41
    # tgravitycorrxz=np.corrcoef(gravity[:,0],gravity[:,2])
    # firstlist.append(tgravitycorrxz[0 , 1])
    # #42
    # tgravitycorryz=np.corrcoef(gravity[:,1],gravity[:,2])
    # firstlist.append(tgravitycorryz[0 , 1])
    # #64
    # tbodyaccmagmean=np.mean(LA.norm(body,axis=1))
    # secondlist.append(tbodyaccmagmean)
    # #65
    # tbodyaccmagstd=np.std(LA.norm(body,axis=1))
    # secondlist.append(tbodyaccmagstd)
    # #66
    # norm=LA.norm(body,axis=1)
    # tbodyaccmagmad=np.mean(np.absolute(norm-np.mean(norm)))
    # secondlist.append(tbodyaccmagmad)
    # #67
    # tbodyaccmagmaxx=np.max(LA.norm(body,axis=1))
    # secondlist.append(tbodyaccmagmaxx)
    # #68
    # tbodyaccmagminx=np.min(LA.norm(body,axis=1))
    # secondlist.append(tbodyaccmagminx)
    # #69
    # norm=LA.norm(body,axis=1)
    # tbodyaccmagiqr=stats.iqr(norm,interpolation="midpoint")
    # secondlist.append(tbodyaccmagiqr)
    # #70
    # tgravityaccmagmean=np.mean(LA.norm(gravity,axis=1))
    # secondlist.append(tgravityaccmagmean)
    # #71
    # tgravityaccmagstd=np.std(LA.norm(gravity,axis=1))
    # secondlist.append(tgravityaccmagstd)
    # #72
    # norm=LA.norm(gravity,axis=1)
    # tgravityaccmagmad=np.mean(np.absolute(norm-np.mean(norm)))
    # secondlist.append(tgravityaccmagmad)
    # # print(tgravityaccmagmad)
    # #73
    # tgravityaccmagmaxx=np.max(LA.norm(gravity,axis=1))
    # secondlist.append(tgravityaccmagmaxx)
    # #74
    # tgravityaccmagminx=np.min(LA.norm(gravity,axis=1))
    # secondlist.append(tgravityaccmagminx)
    # #75
    # norm=LA.norm(gravity,axis=1)
    # tgravityaccmagiqr=stats.iqr(norm,interpolation="midpoint")
    # secondlist.append(tgravityaccmagiqr)
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
    
    # x = gyscope_val[:,[0]].reshape(1,gyscope_val.shape[0])
    # y = gyscope_val[:,[1]].reshape(1,gyscope_val.shape[0])
    # z = gyscope_val[:,[2]].reshape(1,gyscope_val.shape[0])
    # x = x[0]
    # y = y[0]
    # z = z[0]
    # #46
    # tBodyGyro_std_X = np.std(x)
    # gyro_list.append(tBodyGyro_std_X)
    # #47
    # tBodyGyro_std_y = np.std(y)
    # gyro_list.append(tBodyGyro_std_y)
    # #48
    # tBodyGyro_std_z = np.std(z)
    # gyro_list.append(tBodyGyro_std_z)
    # #49
    # tBodyGyro_mad_X = np.mean(np.absolute(x - np.mean(x)))
    # gyro_list.append(tBodyGyro_mad_X)
    # #50
    # tBodyGyro_mad_y = np.mean(np.absolute(y - np.mean(y)))
    # gyro_list.append(tBodyGyro_mad_y)
    # #51
    # tBodyGyro_mad_z = np.mean(np.absolute(z - np.mean(z)))
    # gyro_list.append(tBodyGyro_mad_z)
    # #52
    # gyro_list.append(np.max(x))
    # #53
    # gyro_list.append(np.max(y))
    # #54
    # gyro_list.append(np.max(z))
    # #55
    # gyro_list.append(np.min(x))
    # #56
    # gyro_list.append(np.min(y))
    # #57
    # gyro_list.append(np.min(z))
    # #58
    # gyro_list.append(stats.iqr(x, interpolation = 'midpoint'))
    # #59
    # gyro_list.append(stats.iqr(y, interpolation = 'midpoint'))
    # #60
    # gyro_list.append(stats.iqr(z, interpolation = 'midpoint'))
    # tBodyGyro_correlation_X_Y = np.corrcoef(x, y)
    # tBodyGyro_correlation_X_Z = np.corrcoef(x, z)
    # tBodyGyro_correlation_Y_Z = np.corrcoef(y, z)

    # tBodyGyro_correlation_X_Y = tBodyGyro_correlation_X_Y[0 , 1]
    # #61
    # gyro_list.append(tBodyGyro_correlation_X_Y)

    # tBodyGyro_correlation_X_Z = tBodyGyro_correlation_X_Z[0 , 1]
    # #62
    # gyro_list.append(tBodyGyro_correlation_X_Z)

    # tBodyGyro_correlation_Y_Z = tBodyGyro_correlation_Y_Z[0 , 1]
    # #63
    # gyro_list.append(tBodyGyro_correlation_Y_Z)

    # tBodyGyroMag = LA.norm(gyscope_val, axis=1)
    # #76
    # gyro_list_2.append(np.mean(tBodyGyroMag))
    # #77
    # gyro_list_2.append(np.std(tBodyGyroMag))
    # #78
    # gyro_list_2.append(np.mean(np.absolute(tBodyGyroMag - np.mean(tBodyGyroMag))))
    # #79
    # gyro_list_2.append(np.max(tBodyGyroMag))
    # #80
    # gyro_list_2.append(np.min(tBodyGyroMag))
    # #81
    # gyro_list_2.append(stats.iqr(tBodyGyroMag, interpolation = 'midpoint'))
    
    return gyro_list,gyro_list_2

def extract_features(gyroscope,accelerometer):
    f_1,f_3 = main(accelerometer)
    f_2,f_4 = tbodyjerkgro(gyroscope)
    # f_1.extend(f_2)
    f_1.extend(f_2)
    # f_1.extend(f_4)
    features_cal = f_1
    return features_cal

# input_json = {"gyroscope":[[-0.024859048426151276,0.010373157449066639,0.007467169314622879],[-0.05149063840508461,0.010905790142714977,-0.004250729456543922],[-0.044566426426172256,0.012503684498369694,-0.010109677910804749],[-0.029120102524757385,0.020493159070611,-0.00957704707980156],[-0.01953273080289364,0.0077099986374378204,-0.0218275785446167],[-0.0019558833446353674,0.014634213410317898,-0.03674126788973808],[-0.0008906195871531963,0.030080532655119896,-0.011707574129104614],[0.008164120838046074,0.018895264714956284,-0.003185465931892395],[0.015088332816958427,0.04819001629948616,-0.022892840206623077],[0.015088332816958427,0.050853174179792404,-0.04313284903764725],[-0.0040864101611077785,0.05191843584179878,-0.036208637058734894],[-0.015804307535290718,0.027950003743171692,-0.02555599808692932],[-0.014206413179636002,0.0039815763011574745,0.0048040105029940605],[-0.003553778398782015,0.0023836810141801834,-0.005315992049872875],[0.00017464393749833107,-0.0066710589453577995,-0.005315992049872875],[-0.006749568972736597,0.0039815763011574745,-0.015968628227710724],[-0.01473904587328434,-0.0066710589453577995,-0.019164418801665306],[-0.013673782348632812,-0.004540531896054745,-0.01703389175236225],[-0.01473904587328434,0.008775263093411922,-0.00957704707980156],[0.03159991651773453,0.017297370359301567,-0.0005223072366788983],[0.04278518632054329,0.005046839825809002,0.005336642265319824],[-0.012075886130332947,-0.007736322935670614,-0.001054938999004662],[-0.04403379186987877,-0.008801585994660854,0.0016082198126241565],[-0.00142325134947896,-0.20747323334217072,0.006934537552297115],[0.003903066273778677,-0.40880802273750305,0.1102650985121727],[0.00017464393749833107,-0.37152379751205444,0.11079773306846619],[0.01828412525355816,-0.2037448137998581,0.09322088211774826],[0.06622098386287689,-0.12385004758834839,0.030370334163308144],[0.08646099269390106,-0.06259739398956299,-0.030882317572832108],[0.08699362725019455,-0.08230477571487427,-0.03301284462213516],[0.05823150649666786,-0.184037446975708,0.0277071762830019],[-0.024859048426151276,-0.08177213370800018,0.024511385709047318],[0.023077810183167458,0.050853174179792404,-0.03780652955174446],[0.08646099269390106,0.0023836810141801834,-0.05165495350956917],[0.06355782598257065,0.0156994741410017,-0.018631786108016968],[0.010827280580997467,0.010905790142714977,0.02823980711400509],[-0.01047799177467823,-0.0013447412056848407,0.02823980711400509],[-0.00568430544808507,0.013568948023021221,0.012260855175554752],[-0.01846746727824211,0.026352109387516975,0.01492401398718357],[-0.006216937210410833,0.01996052823960781,0.003738746978342533],[-0.025924311950802803,0.010373157449066639,0.007999801076948643],[-0.053088534623384476,0.018895264714956284,0.015456645749509335],[-0.045631688088178635,0.021025793626904488,0.0016082198126241565],[0.006033593323081732,0.02475421503186226,-0.012772835791110992],[0.05237255617976189,0.05298370122909546,-0.018631786108016968],[0.04811150208115578,0.02901526726782322,-0.003185465931892395],[0.024675704538822174,-0.00027947771013714373,0.007467169314622879],[-0.02326115220785141,0.00025315405218861997,-0.014370733872056007],[-0.029120102524757385,-0.00027947771013714373,-0.028219159692525864],[0.024143071845173836,0.025819478556513786,-0.0026528341695666313],[0.06835151463747025,0.029547901824116707,0.020250331610441208],[0.03905675932765007,0.008242630399763584,0.021848227828741074],[0.009229382500052452,-0.030639488250017166,0.0032061152160167694],[0.03532833978533745,-0.018921589478850365,-0.007446520030498505],[0.049176763743162155,0.02422158233821392,-0.007446520030498505],[0.11362520605325699,0.02368895150721073,0.0032061152160167694],[0.15303994715213776,0.06257106363773346,-0.014370733872056007],[0.13919152319431305,0.07215844094753265,-0.04153495281934738],[0.040654655545949936,0.03540685027837753,-0.03514336794614792],[-0.05255590006709099,-0.0018773729680106044,-0.020229680463671684],[-0.03657694533467293,0.00984052661806345,-0.035676002502441406],[0.033197809010744095,0.02901526726782322,-0.036208637058734894],[0.05024202540516853,0.03167843073606491,-0.02236020937561989],[-0.014206413179636002,-0.014127903617918491,-0.0026528341695666313]],"accelerometer":[[-0.2602822780609131,-0.0386289618909359,-0.023425474762916565],[-0.37106969952583313,-0.08603318780660629,-0.001054938999004662],[-0.41154971718788147,-0.08123950660228729,-0.027686525136232376],[-0.47493287920951843,-0.05407528206706047,-0.047926533967256546],[-0.5761329531669617,-0.12012162059545517,-0.03407810628414154],[-0.5910466313362122,-0.06632581353187561,-0.0596444308757782],[-0.5292613506317139,0.04126580059528351,-0.08947180956602097],[-0.4483012855052948,-0.03330264613032341,-0.07242759317159653],[-0.3439054787158966,-0.09455530345439911,-0.09000443667173386],[-0.2453686147928238,0.02368895150721073,-0.12835393846035004],[-0.187844380736351,0.0322110615670681,-0.09905917942523956],[-0.12020013481378555,0.0370047464966774,-0.03461073711514473],[-0.048827480524778366,-0.000812109443359077,0.005336642265319824],[0.006033593323081732,-0.011997376568615437,0.029305070638656616],[0.053970444947481155,-0.02105211652815342,0.050077710300683975],[0.0891241505742073,-0.017856325954198837,0.04954507574439049],[0.1178862601518631,0.01623210683465004,0.04847981408238411],[0.1130925789475441,0.008242630399763584,0.05327349901199341],[0.07207993417978287,-0.0173236932605505,0.06073034554719925],[0.041719917207956314,0.02901526726782322,0.05327349901199341],[0.0140230692923069,0.16590163111686707,0.022380858659744263],[-0.11753696948289871,0.3725627660751343,-0.048991795629262924],[-0.1846485733985901,-0.05141212418675423,0.0005429562879726291],[-0.1138085424900055,-0.14515532553195953,-0.008511783555150032],[-0.006749568972736597,-0.14515532553195953,0.04262086749076843],[0.02627360075712204,-0.1659279614686966,0.09801456332206726],[0.04811150208115578,-0.1419595330953598,0.09854719787836075],[0.06675361841917038,-0.07378266006708145,0.062328241765499115],[0.08646099269390106,-0.02051948383450508,0.029837703332304955],[0.0987115204334259,0.006644735112786293,0.0016082198126241565],[0.09764625877141953,0.0013184176059439778,0.030902966856956482],[0.0518399216234684,0.01676473766565323,0.037294548004865646],[0.008164120838046074,0.0039815763011574745,0.04102297127246857],[-0.022195890545845032,-0.03703106567263603,0.03409875929355621],[-0.01900009997189045,-0.0855005607008934,0.021848227828741074],[-0.032848525792360306,-0.08869635313749313,0.017587173730134964],[-0.07652432471513748,-0.055673178285360336,0.01492401398718357],[-0.12020013481378555,-0.06526055186986923,0.037294548004865646],[-0.08238327503204346,-0.059934232383966446,-0.011707574129104614],[-0.06746958196163177,-0.013595270924270153,-0.022892840206623077],[-0.08877485245466232,-0.03756370022892952,-0.01756652258336544],[-0.08291590958833694,0.0013184176059439778,0.008532432839274406],[-0.029120102524757385,-0.00241000484675169,-0.022892840206623077],[0.020947283133864403,-0.05460791662335396,-0.028219159692525864],[0.027871496975421906,-0.011464743874967098,-0.019697049632668495],[0.023610441014170647,0.060440544039011,0.03835981339216232],[0.036926236003637314,0.0013184176059439778,0.062860868871212],[0.04278518632054329,-0.03703106567263603,0.03196822851896286],[0.033197809010744095,-0.04182475060224533,0.03250086307525635],[0.027871496975421906,0.008775263093411922,0.03995770588517189],[0.020414650440216064,0.02848263643682003,0.01492401398718357],[-0.007814832031726837,0.00984052661806345,0.011728223413228989],[-0.024859048426151276,-0.03330264613032341,0.0005429562879726291],[-0.03924011066555977,-0.01466053444892168,-0.010642310604453087],[-0.06374116241931915,-0.018921589478850365,0.0010755880502983928],[-0.0802527442574501,-0.02531317062675953,0.01332611870020628],[-0.1138085424900055,0.00025315405218861997,0.022380858659744263],[-0.155353844165802,-0.055673178285360336,0.018652435392141342],[-0.1846485733985901,-0.01625843159854412,-0.01809915527701378],[-0.18571384251117706,0.0039815763011574745,-0.032480210065841675],[0.09764625877141953,-0.06579318642616272,0.26366305351257324],[0.22920629382133484,-0.44715753197669983,0.27751147747039795],[0.24731576442718506,-0.3369027376174927,0.09375350922346115],[0.18659573793411255,-0.19309218227863312,-0.06497074663639069]]}
# data= extract_features(np.array(input_json['gyroscope']),np.array(input_json['accelerometer']))
# shape = list(np.array(input_json['gyroscope']).shape)
# print(data)
# import pickle
# loaded_model = pickle.load(open('lrmodel (5).pkl', 'rb'))
# outputlabel=['LAYING','SITTING','STANDING','WALKING','WALKING_DOWNSTAIRS','WALKING_UPSTAIRS']
# data = np.array(data)
# pred = outputlabel[int(loaded_model.predict(data.reshape(1,9)))]
# print(pred)

def concat(data):
    
    # Select left pocket data
    
    #Square root of sum of squares of accelerometer, linear acceleration and gyroscope data
    data["MA"] = np.sqrt(np.square(data['Ax']) + np.square(data['Ay']) + np.square(data['Az']))
    data["ML"] = np.sqrt(np.square(data['Lx']) + np.square(data['Ly']) + np.square(data['Lz']))
    data["MG"] = np.sqrt(np.square(data['Gx']) + np.square(data['Gy']) + np.square(left_pocket['Gz']))
   
    return data

def generate_sequence(x,n_time_steps, step):
    
    segments = []
    for i in range(0, len(x) - n_time_steps, step):
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

def reshape_segments(x, y, n_time_steps, n_features):
    x_reshaped = np.asarray(x, dtype= np.float32).reshape(-1, n_time_steps, n_features)
    return x_reshaped
