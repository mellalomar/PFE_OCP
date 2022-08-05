from numpy import NaN
import sklearn as sk
import pandas as pd
from pathlib import Path
import os
import sys

from django.core.management.base import BaseCommand, CommandError
from OCP.models import Detail

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        names =["Date","SM-BO","SM-MZ","MAT-NIF","SFA","DSP","C2 Sup","C4 inf","C5 supA","C5 inf","C6 s+m","C6 inf","BPL","MgO","Fe2O3","SiO2","CO2","BPLnif","MgOnif","Fe2O3nif","SiO2nif","CO2nif"]
        df_2021 = pd.read_csv("OCP/data/data2021.csv",sep=';',names=names)
        df_2022 = pd.read_csv("OCP/data/data2022.csv",sep=';',names=names)
        df = pd.concat([df_2021,df_2022])

        
        df = df.replace(NaN,0)
        df = df.replace(' -     ',0)
        
        SM_BO = df[df['SM-BO'] != 0]
        SM_BO =  SM_BO.drop(["Date","SM-MZ","MAT-NIF","SFA","DSP","C2 Sup","C4 inf","C5 supA","C5 inf","C6 s+m","C6 inf"],axis=1)
        print(len(SM_BO))
        
        SM_MZ = df[df['SM-MZ'] != 0]
        SM_MZ =  SM_MZ.drop(['Date', 'SM-BO', 'MAT-NIF', 'SFA', 'DSP', 'C2 Sup', 'C4 inf','C5 supA', 'C5 inf', 'C6 s+m', 'C6 inf'],axis=1)
        print(len(SM_MZ))

        SM_NIF = df[df['MAT-NIF'] != 0]
        SM_NIF =  SM_NIF.drop(["Date","SM-BO","SM-MZ","SFA","DSP","C2 Sup","C4 inf","C5 supA","C5 inf","C6 s+m","C6 inf"],axis=1)
        print(len(SM_NIF))

        SFA = df[df['SFA'] != 0]
        SFA =  SFA.drop(["Date","SM-BO","MAT-NIF","SM-MZ","DSP","C2 Sup","C4 inf","C5 supA","C5 inf","C6 s+m","C6 inf"],axis=1)
        print(len(SFA))

        DSP = df[df['DSP'] != 0]
        DSP =  DSP.drop(["Date","SM-BO","MAT-NIF","SFA","SM-MZ","C2 Sup","C4 inf","C5 supA","C5 inf","C6 s+m","C6 inf"],axis=1)
        print(len(DSP))

        C2_Sup = df[df['C2 Sup'] != 0]
        C2_Sup =  C2_Sup.drop(["Date","SM-BO","MAT-NIF","SFA","DSP","SM-MZ","C4 inf","C5 supA","C5 inf","C6 s+m","C6 inf"],axis=1)
        print(len(C2_Sup))

        C4_inf = df[df['C4 inf'] != 0]
        C4_inf =  C4_inf.drop(["Date","SM-BO","MAT-NIF","SFA","DSP","C2 Sup","SM-MZ","C5 supA","C5 inf","C6 s+m","C6 inf"],axis=1)
        print(len(C4_inf))

        C5_supA = df[df['C5 supA'] != 0]
        C5_supA =  C5_supA.drop(["Date","SM-BO","MAT-NIF","SFA","DSP","C2 Sup","C4 inf","SM-MZ","C5 inf","C6 s+m","C6 inf"],axis=1)
        print(len(C5_supA))

        C5_inf = df[df['C5 inf'] != 0]
        C5_inf =  C5_inf.drop(["Date","SM-BO","MAT-NIF","SFA","DSP","C2 Sup","C4 inf","C5 supA","SM-MZ","C6 s+m","C6 inf"],axis=1)
        print(len(C5_inf))


        C6_sm = df[df['C6 s+m'] != 0]
        C6_sm =  C6_sm.drop(["Date","SM-BO","MAT-NIF","SFA","DSP","C2 Sup","C4 inf","C5 supA","C5 inf","SM-MZ","C6 inf"],axis=1)
        print(len(C6_sm))

        C6_inf = df[df['C6 inf'] != 0]
        C6_inf =  C6_inf.drop(["Date","SM-BO","MAT-NIF","SFA","DSP","C2 Sup","C4 inf","C5 supA","C5 inf","C6 s+m","SM-MZ"],axis=1)
        print(len(C6_inf))



        #"Date","SM-BO","SM-MZ","MAT-NIF","SFA","DSP","C2 Sup","C4 inf","C5 supA","C5 inf","C6 s+m","C6 inf","BPL","MgO","Fe2O3","SiO2","CO2","BPLnif","MgOnif","Fe2O3nif","SiO2nif","CO2nif"

        #df.to_csv("OCP/data/data.csv")
        #print(df.columns)
        #print(df.head())