
import os
from AerosolAutomate import AutomateAerosolRF
param={}
WAparam={}
NAparam={}
# default values
param['alat']='22.6'
param['alon']='88.4'
param['wlinf']='0.25'
param['wlsup']='4.0'
param['wlinc']='0.025'
param['isalb']='10'
param['sc']='0,0.6,0.15,0.25'
param['uw']='3.234'
param['uo3']='0.263'
param['xco2']='380.0000'
param['xch4']='1.7400'
param['xn2o']='0.3200'
param['wlbaer']='0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.90,1.00,1.25,1.50,1.75,2.00,2.50,3.00,3.20,3.39,3.50,3.75,4.00'
param['iaer']='0'
param['jaer']='0'
param['idatm']='1'
param['iday']='330'
param['iout']='10'
param['nstr']='8'

'''
WAparam['wbaer']='0.68,0.73,0.73,0.72,0.72,0.71,0.71,0.71,0.70,0.70,0.69,0.67,0.66,0.64,0.60,0.58,0.56,0.56,0.53,0.34,0.48,0.55,0.57,0.63,0.69'
WAparam['gbaer']='0.70,0.68,0.67,0.67,0.67,0.66,0.66,0.66,0.65,0.65,0.65,0.65,0.65,0.65,0.65,0.66,0.68,0.70,0.74,0.77,0.75,0.74,0.74,0.73,0.72'
WAparam['qbaer']='1.23,1.08,0.93,0.80,0.70,0.62,0.54,0.48,0.44,0.39,0.36,0.33,0.28,0.24,0.18,0.15,0.12,0.11,0.09,0.12,0.10,0.09,0.08,0.08,0.08'

NAparam['wbaer']='7.04E-01,7.82E-01,7.91E-01,7.86E-01,7.83E-01,7.77E-01,7.73E-01,7.71E-01,7.61E-01,7.59E-01,7.48E-01,7.33E-01,7.11E-01,6.95E-01,6.55E-01,6.33E-01,6.29E-01,6.37E-01,6.01E-01,5.09E-01,5.92E-01,6.27E-01,6.44E-01,7.02E-01,7.64E-01'
NAparam['gbaer']='6.82E-01,6.52E-01,6.43E-01,6.38E-01,6.34E-01,6.29E-01,6.27E-01,6.24E-01,6.22E-01,6.20E-01,6.20E-01,6.23E-01,6.24E-01,6.26E-01,6.43E-01,6.60E-01,6.88E-01,7.16E-01,7.46E-01,7.95E-01,7.72E-01,7.62E-01,7.56E-01,7.42E-01,7.25E-01'
NAparam['qbaer']='1.23, 1.08, 0.93, 0.80, 0.70, 0.62, 0.54, 0.48, 0.44, 0.39, 0.36, 0.33, 0.28, 0.24, 0.18, 0.15, 0.12, 0.11, 0.09, 0.12, 0.10, 0.09, 0.08, 0.08, 0.08'

'''
def DeleteFile(file):
    cwd=os.getcwd()
    path=os.path.join(cwd,"Data",file)
    #print(path)
    if os.path.exists(path):
        os.remove(path)

def Script(cmdict,m,ind):
    with open('inputs.sh', m) as f:
        if ind==0:
            f.write('echo running SBDART for aerosol\n')
            param['iaer']='5'
        else:
            param['iaer']='0'
            f.write('echo running SBDART for no aerosol\n')
        f.write("for time in 0. 1. 2. 3. 4. 5. 6. 7. 8. 9. 10. 11. 12. 13. 14. 15. 16. 17. 18. 19. 20. 21. 22. 23. ;do\n")
        f.write('{} {}\n'.format('echo', '"'))
        f.write("&INPUT\n")
        f.write('  time=$time\n')
        for key, value in param.items():
            f.write('  {}={}\n'.format(key, value))
        for key, value in cmdict.items():
            f.write('  {}={}\n'.format(key, value))
        f.write('/{}>INPUT\n'.format('"'))
        if ind==0:
            f.write('./sbdart >>./Data/wa.out\n')
        else:
            f.write('./sbdart >>./Data/na.out\n')
        f.write('done\n')
    

def AerosolScript(cmdict):
    DeleteFile("wa.out")
    Script(cmdict,'w',0)
    x=os.system('chmod +x inputs.sh')
    if  x==0:
        x=os.system('./inputs.sh')
        if x==0:
            at=AutomateAerosolRF('wa')
            at.Result()
            return True
    return False

    

def WithoutAerosolScript(cmdict):
    DeleteFile("na.out")
    Script(cmdict,'w',1)
    
    x=os.system('chmod +x inputs.sh')
    if  x==0:
        x=os.system('./inputs.sh')
        if x==0:
            at=AutomateAerosolRF('na')
            at.Result()
            return True
    return False

def BothScript(cmdict1,cmdict2):
    DeleteFile('wa.out')
    DeleteFile('na.out')
    Script(cmdict1,'w',0)
    Script(cmdict2,'a',1)
    
    x=os.system('chmod +x inputs.sh')
    if  x==0:
        x=os.system('./inputs.sh')
        if x==0:
            at=AutomateAerosolRF('both')
            at.Result()
            return True
    return False
       
#xxDeleteFile('wa.out')
#BothScript(WAparam,NAparam)
