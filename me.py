def round_up(num):
    num = int(num * 100)
    if (num % 10 > 0):
        num = num + 10 - num % 10
    return num / 100


def Dangerlevel(BaseScore):
    if BaseScore == 0:
        print('Безопасно')
    if BaseScore >= 0.1 and BaseScore <= 3.9:
        print('Низкий уровень опасности')
    if BaseScore >= 4 and BaseScore <= 6.9:
        print('Средний уровень опасности')
    if BaseScore >= 7 and BaseScore <= 8.9:
        print('Высокий уровень опасности')
    if BaseScore >= 9:
        print('Критический уровень опасности')


AV = float(input('Пожалуйста, введите AV: \n'))
AC = float(input('Пожалуйста, введите AC: \n'))
PR = float(input('Пожалуйста, введите PR: \n'))
UI = float(input('Пожалуйста, введите UI: \n'))
S = float(input('Пожалуйста, введите S: \n'))
C = float(input('Пожалуйста, введите C: \n'))
I = float(input('Пожалуйста, введите I: \n'))
A = float(input('Пожалуйста, введите A: \n'))

ImpactBase = 1 - ((1 - C) * (1 - I) * (1 - A))
Exploitability = 8.22 * AV * AC * PR * UI

if (S == 0):
    Impact = 6.42 * ImpactBase
else:
    Impact = 7.52 * (ImpactBase - 0.029) - 3.25 * (ImpactBase - 0.02)**15

if (Impact <= 0):
    BaseScore = 0
else:
    if (S == 0):
        BaseScore =round_up(min(ImpactBase + Exploitability, 10))**2
    if (S == 1):
        BaseScore=round_up(min(1.08 * (ImpactBase + Exploitability), 10))


print('---------- \n')
print('BaseScore=', BaseScore)
print('---------- \n')
Dangerlevel(BaseScore)

print('---------- \n')
print('\n')
print('For TimeMitric')
print('\n')

E=float(input('Пожалуйста, введите E: \n'))
RL=float(input('Пожалуйста, введите RL: \n'))
RC=float(input('Пожалуйста, введите RC: \n'))

TemporalScore=round_up(BaseScore*E*RL*RC)

print('---------- \n')
print('TimeMitric=',TemporalScore)

print('---------- \n')
print('\n')
print('For Contextualmetric')
print('\n')

MAV=float(input('Пожалуйста, введите MAV: \n'))
MAC=float(input('Пожалуйста, введите MAC: \n'))
MPR=float(input('Пожалуйста, введите MPR: \n'))
MUI=float(input('Пожалуйста, введите MUI: \n'))
MS=float(input('Пожалуйста, введите MS: \n'))
MC=float(input('Пожалуйста, введите MC: \n'))
MI=float(input('Пожалуйста, введите MI: \n'))
MA=float(input('Пожалуйста, введите MA: \n'))
CR=float(input('Пожалуйста, введите CR: \n'))
IR=float(input('Пожалуйста, введите IR: \n'))
AR=float(input('Пожалуйста, введите AR: \n'))

MExploitability=8.22*MAV*MAC*MPR*MUI
MImpactBase=min((1-(1-MC*CR)*(1-MI*IR)*(1-MA*AR)),0.915)
if (MS==1):
    MImpact=7.52*(MImpactBase-0.029)-3.25*(MImpactBase-0.02)**15
else:
    MImpact=6.42*MImpactBase
if (MImpact<0):
    EnvironmentalScore=0
else:
    if (MS==0):
        EnvironmentalScore=round_up(round_up(min(MImpact+MExploitability,10))*E*RL*RC)
    else:
        EnvironmentalScore=round_up(round_up(min(1.08*(MImpact+MExploitability),10))*E*RL*RC)
    
print('---------- \n')
print('Contextualmetric=',EnvironmentalScore)
print('---------- \n')
print('\n')
