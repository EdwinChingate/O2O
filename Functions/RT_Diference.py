import numpy as np
def RT_Diference(SignalsMat):#With filters for mz and RT
    NumberofCandidates=len(SignalsMat)
    DifRT=np.zeros([NumberofCandidates,NumberofCandidates])
    FirstCandidate=True
    for candidatePos in np.arange(NumberofCandidates):       
        RT_candidate=SignalsMat[candidatePos,7]
        RT_Dif=abs(RT_candidate-SignalsMat[:,7])
        DifRT[candidatePos,:]=RT_Dif
    return DifRT

