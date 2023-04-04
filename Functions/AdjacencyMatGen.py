import numpy as np
from mz_Diference import *
from RT_Diference import *
#Replacing the clustring strategy with the minimum distance
def AdjacencyMatGen(SignalsMat,MinNumberCandidatesClustering=5,max_mz_Tol=1e-2,max_RT_Tol=0.3):
    DifRT=RT_Diference(SignalsMat)
    Difmz=mz_Diference(SignalsMat)
    NumberofCandidates=len(DifRT)
    AdjacencyMatrix=np.zeros([NumberofCandidates,NumberofCandidates])
    for candidatePos in np.arange(NumberofCandidates):
        NeighborsLoc=np.where((DifRT[candidatePos,:]<max_RT_Tol)&(Difmz[candidatePos,:]<max_mz_Tol))[0]
        AdjacencyMatrix[candidatePos,NeighborsLoc]=1
    return AdjacencyMatrix