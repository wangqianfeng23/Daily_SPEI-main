import utilsPY as utils
import numpy as np
import pandas as pd

def cal2_SPEI(
        pre: np.ndarray,
        scale: int,
        type: str,
):
    culpre = utils.scale_values_spei(pre, scale, type)
    f_alpa, f_beta, f_P0 = utils.fit_gev_para(culpre)
    rawSPEI = utils.caculate_SPEI_gev(culpre, f_alpa, f_beta, f_P0)
    SPEI = np.clip(rawSPEI, -3, 3).flatten()
    return SPEI



#Daily SPEI
inputfile=r'I:\upload\code\Daily_SPI_and_SPEI-main\prepet031_394.csv'
data=pd.read_csv(inputfile)
culpre = utils.scale_values_spei(np.array(data['pre-pet']), 30, 'daily')
f_alpa, f_beta, f_P0 = utils.fit_gev_para(culpre)
rawSPEI = utils.caculate_SPEI_gev(culpre, f_alpa, f_beta, f_P0)
SPEI = np.clip(rawSPEI, -3, 3).flatten()
outSPEI=pd.DataFrame({'Date':data['date'],'SPEI':SPEI})
outSPEI.to_csv(r'I:\upload\code\Daily_SPI_and_SPEI-main\1\SPEI031_394.csv')


