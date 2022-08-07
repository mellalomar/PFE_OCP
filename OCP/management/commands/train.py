from numpy import NaN
import sklearn as sk
import pandas as pd
from sklearn.utils import resample
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.model_selection import train_test_split


from django.core.management.base import BaseCommand, CommandError
from OCP.models import Detail

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        names =["Date","SM-BO","SM-MZ","MAT-NIF","SFA","DSP","C2 Sup","C4 inf","C5 supA","C5 inf","C6 s+m","C6 inf","BPL","MgO","Fe2O3","SiO2","CO2","BPLnif","MgOnif","Fe2O3nif","SiO2nif","CO2nif"]
        df_2021 = pd.read_csv("OCP/data/data2021.csv",sep=';',names=names,header=1)
        df_2022 = pd.read_csv("OCP/data/data2022.csv",sep=';',names=names,header=1)
        df = pd.concat([df_2021,df_2022])

        
        df = df.replace(NaN,0)
        df = df.replace(' -     ',0)
        
        SM_BO = df[df['SM-BO'] != 0]
        SM_BO =  SM_BO.drop(["Date","SM-MZ","MAT-NIF","SFA","DSP","C2 Sup","C4 inf","C5 supA","C5 inf","C6 s+m","C6 inf"],axis=1)
        SM_BO = resample(SM_BO,replace=True,n_samples=500,random_state=len(SM_BO)-1)
        print(len(SM_BO))
        
        
        SM_MZ = df[df['SM-MZ'] != 0]
        SM_MZ =  SM_MZ.drop(['Date', 'SM-BO', 'MAT-NIF', 'SFA', 'DSP', 'C2 Sup', 'C4 inf','C5 supA', 'C5 inf', 'C6 s+m', 'C6 inf'],axis=1)
        SM_MZ = resample(SM_MZ,replace=True,n_samples=500,random_state=len(SM_MZ)-1)
        print(len(SM_MZ))

        SM_NIF = df[df['MAT-NIF'] != 0]
        SM_NIF =  SM_NIF.drop(["Date","SM-BO","SM-MZ","SFA","DSP","C2 Sup","C4 inf","C5 supA","C5 inf","C6 s+m","C6 inf"],axis=1)
        SM_NIF = resample(SM_NIF,replace=True,n_samples=500,random_state=len(SM_NIF)-1)
        print(len(SM_NIF))

        SFA = df[df['SFA'] != 0]
        SFA =  SFA.drop(["Date","SM-BO","MAT-NIF","SM-MZ","DSP","C2 Sup","C4 inf","C5 supA","C5 inf","C6 s+m","C6 inf"],axis=1)
        SFA = resample(SFA,replace=True,n_samples=500,random_state=len(SFA)-1)
        print(len(SFA))

        DSP = df[df['DSP'] != 0]
        DSP =  DSP.drop(["Date","SM-BO","MAT-NIF","SFA","SM-MZ","C2 Sup","C4 inf","C5 supA","C5 inf","C6 s+m","C6 inf"],axis=1)
        DSP = resample(DSP,replace=True,n_samples=500,random_state=len(DSP)-1)
        print(len(DSP))

        C2_Sup = df[df['C2 Sup'] != 0]
        C2_Sup =  C2_Sup.drop(["Date","SM-BO","MAT-NIF","SFA","DSP","SM-MZ","C4 inf","C5 supA","C5 inf","C6 s+m","C6 inf"],axis=1)
        C2_Sup = resample(C2_Sup,replace=True,n_samples=500,random_state=len(C2_Sup)-1)
        print(len(C2_Sup))

        C4_inf = df[df['C4 inf'] != 0]
        C4_inf =  C4_inf.drop(["Date","SM-BO","MAT-NIF","SFA","DSP","C2 Sup","SM-MZ","C5 supA","C5 inf","C6 s+m","C6 inf"],axis=1)
        C4_inf = resample(C4_inf,replace=True,n_samples=500,random_state=len(C4_inf)-1)
        print(len(C4_inf))

        C5_supA = df[df['C5 supA'] != 0]
        C5_supA =  C5_supA.drop(["Date","SM-BO","MAT-NIF","SFA","DSP","C2 Sup","C4 inf","SM-MZ","C5 inf","C6 s+m","C6 inf"],axis=1)
        C5_supA = resample(C5_supA,replace=True,n_samples=500,random_state=len(C5_supA)-1)
        print(len(C5_supA))

        C5_inf = df[df['C5 inf'] != 0]
        C5_inf =  C5_inf.drop(["Date","SM-BO","MAT-NIF","SFA","DSP","C2 Sup","C4 inf","C5 supA","SM-MZ","C6 s+m","C6 inf"],axis=1)
        C5_inf = resample(C5_inf,replace=True,n_samples=500,random_state=len(C5_inf)-1)
        print(len(C5_inf))


        C6_sm = df[df['C6 s+m'] != 0]
        C6_sm =  C6_sm.drop(["Date","SM-BO","MAT-NIF","SFA","DSP","C2 Sup","C4 inf","C5 supA","C5 inf","SM-MZ","C6 inf"],axis=1)
        C6_sm = resample(C6_sm,replace=True,n_samples=500,random_state=len(C6_sm)-1)
        print(len(C6_sm))

        C6_inf = df[df['C6 inf'] != 0]
        C6_inf =  C6_inf.drop(["Date","SM-BO","MAT-NIF","SFA","DSP","C2 Sup","C4 inf","C5 supA","C5 inf","C6 s+m","SM-MZ"],axis=1)
        C6_inf = resample(C6_inf,replace=True,n_samples=500,random_state=len(C6_inf)-1)
        print(len(C6_inf))

        Y_col = 'SM-BO'
        X_cols = ["BPL","MgO","Fe2O3","SiO2","CO2"]
        X, y = SM_BO[X_cols] , SM_BO[Y_col]
        print(X.head())
        print(y)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


        n_samples, n_features = 10, 5
        rng = np.random.RandomState(0)
        y = rng.randn(n_samples)
        X = rng.randn(n_samples, n_features)
        regr = make_pipeline(StandardScaler(), SVR(C=1.0, epsilon=0.2))
        regr.fit(X, y)

        #"Date","SM-BO","SM-MZ","MAT-NIF","SFA","DSP","C2 Sup","C4 inf","C5 supA","C5 inf","C6 s+m","C6 inf","BPL","MgO","Fe2O3","SiO2","CO2","BPLnif","MgOnif","Fe2O3nif","SiO2nif","CO2nif"

        #df.to_csv("OCP/data/data.csv")
        #print(df.columns)
        #print(df.head())