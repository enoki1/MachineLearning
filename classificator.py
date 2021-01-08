import numpy as np
import pandas as pd
import time

start_time = time.time()
kills = pd.read_csv('./kill_match_stats_final_0.csv') # traindata
testkills = pd.read_csv('./kill_match_stats_final_3.csv') # testdata

kills = kills.dropna(axis = 0, how = "any")
kills = kills.loc[~kills['killed_by'].isin(['Down and Out'])]
kills = kills.loc[~kills['killed_by'].isin(['Falling'])]
kills = kills.loc[~kills['killed_by'].isin(['Bluezone'])]
kills = kills.loc[~kills['killed_by'].isin(['Hit by Car'])]
kills = kills.loc[~kills['victim_position_x'].isin([0.0])]
kills = kills.loc[~kills['killed_by'].isin(['death.WeapSawnoff_C'])]

kills["kill_distance"] = ((kills["killer_position_x"] - kills["victim_position_x"]) ** 2 + (kills["killer_position_y"] - kills["victim_position_y"]) ** 2) ** (1/2)


killsSW0 = kills.loc[((kills['killed_by'] == "P92") | (kills['killed_by'] == "P1911") | (kills['killed_by'] == "R1895") | (kills['killed_by'] == "R45") | (kills['killed_by'] == "P18C") )& (kills['kill_distance'] <= 2500.0)]
killsSW1 = kills.loc[((kills['killed_by'] == "Pan") | (kills['killed_by'] == "Machete") | ( kills['killed_by'] == "Sickle") | (kills['killed_by'] == "Scrap") | (kills['killed_by'] == "Punch")) & (kills['kill_distance'] <= 300.0)]
killsSW2 = kills.loc[((kills['killed_by'] == "S686") | (kills['killed_by'] == "S12K") | (kills['killed_by'] == "S1897")) & (kills['kill_distance'] <= 2500.0)]
killsSW3 = kills.loc[((kills['killed_by'] == "AKM") | (kills['killed_by'] == "M416") | (kills['killed_by'] == "AUG") | (kills['killed_by'] == "Groza") | (kills['killed_by'] == "M16A4") | (kills['killed_by'] == "SCAR-L")) & (kills['kill_distance'] <= 12000.0)]
killsSW4 = kills.loc[((kills['killed_by'] == "Kar98k") | (kills['killed_by'] == "AWM") | (kills['killed_by'] == "M24")) & (kills['kill_distance'] <= 50000.0)]
killsSW5 = kills.loc[((kills['killed_by'] == "UMP9") | (kills['killed_by'] == "Micro UZI") | (kills['killed_by'] == "Tommy Gun") | (kills['killed_by'] == "Vector")) & (kills['kill_distance'] <= 6500.0)]
killsSW6 = kills.loc[((kills['killed_by'] == "Mini 14") | (kills['killed_by'] == "Mk14") | (kills['killed_by'] == "SKS") | (kills['killed_by'] == "VSS")) & (kills['kill_distance'] <= 35000.0)]
killsSW7 = kills.loc[(kills['killed_by'] == "Grenade") & (kills['kill_distance'] != 0.0) & (kills['kill_distance'] <= 4000.0)]
average = []

average.append(killsSW0['kill_distance'].mean())
average.append(killsSW1['kill_distance'].mean())
average.append(killsSW2['kill_distance'].mean())
average.append(killsSW3['kill_distance'].mean())
average.append(killsSW4['kill_distance'].mean())
average.append(killsSW5['kill_distance'].mean())
average.append(killsSW6['kill_distance'].mean())
average.append(killsSW7['kill_distance'].mean())

print("Average Grenade: " + str(average[7]))
print("Average pistol: " + str(average[0]))
print("Average Cold: " + str(average[1]))
print("Average Shotgun: " + str(average[0]))
print("Average Riffle: " + str(average[1]))
print("Average Sniper(Balt) : " + str(average[4]))
print("Average PP: " + str(average[5]))
print("Average Sniper(Marks) : " + str(average[6]))

weapons_types = ['pistol','Cold','Shotgun', 'Riffle', 'Sniper(Balt)','PP','Sniper(Marks)', 'Grenade']

'''

# ищу самый близкий к одному из средних, к нему и отношу объект
'''
numberofkills = []
numberofkills.append(np.shape(kills)[0])
numberofkills.append(np.shape(killsSW0)[0])
numberofkills.append(np.shape(killsSW1)[0])
numberofkills.append(np.shape(killsSW2)[0])
numberofkills.append(np.shape(killsSW3)[0])
numberofkills.append(np.shape(killsSW4)[0])
numberofkills.append(np.shape(killsSW5)[0])
numberofkills.append(np.shape(killsSW6)[0])
numberofkills.append(np.shape(killsSW7)[0])
for i in range(len(numberofkills)):
    print(numberofkills[i])
# из второго датасета мне нужно смотря лишь на расстояния между игроками пытаться предсказывать из какого оружия было сделано убийство
# при спорных значениях мне нужно отдавать предпочтения тому типу оружия, который чаще появляется в этих диапазонах, но как?
# например, при подсчете среднеей дистанции поражения, выяснилось, что среднее значение дистанции у пистолетов и дробовиков почти совпадает
# обе величины в районе 6м. Если мне на вход придет такой случай, то с большей вероятностью это убийство с дробовика(так как с него было сделано
# почти в 4 раза больше убийств, чем с пистолета. Аналогично с штурмовыми винтовками и гранатой, но с ними должно быть точнее. Так как
# всего 78к убийств сделано гранатой, а штурмовыми винтовками около 4,5млн, не сильно должно повлиять на статистику.
# Классифицировать снайперские винтовки легче всего, разница в дистанции большая, даже в сравнении с марксманскими винтовками.

testkills = testkills.dropna(axis = 0, how = "any")
testkills = testkills.loc[~testkills['killed_by'].isin(['Down and Out'])]
testkills = testkills.loc[~testkills['killed_by'].isin(['Falling'])]
testkills = testkills.loc[~testkills['killed_by'].isin(['Bluezone'])]
testkills = testkills.loc[~testkills['killed_by'].isin(['Hit by Car'])]
testkills = testkills.loc[~testkills['victim_position_x'].isin([0.0])]
testkills = testkills.loc[~testkills['killed_by'].isin(['death.WeapSawnoff_C'])]

testkills["kill_distance"] = ((testkills["killer_position_x"] - testkills["victim_position_x"]) ** 2 + (testkills["killer_position_y"] - testkills["victim_position_y"]) ** 2) ** (1/2)

killsS0 = testkills.loc[((testkills['killed_by'] == "P92") | (testkills['killed_by'] == "P1911") | (testkills['killed_by'] == "R1895") | (testkills['killed_by'] == "R45") | (kills['killed_by'] == "P18C"))]
killsS1 = testkills.loc[((testkills['killed_by'] == "Pan") | (testkills['killed_by'] == "Machete") | (testkills['killed_by'] == "Sickle") | (testkills['killed_by'] == "Scrap") | (kills['killed_by'] == "Punch"))]
killsS2 = testkills.loc[((testkills['killed_by'] == "S686") | (testkills['killed_by'] == "S12K") | (testkills['killed_by'] == "S1897")) & (testkills['kill_distance'] <= 2500.0)]
killsS3 = testkills.loc[((testkills['killed_by'] == "AKM") | (testkills['killed_by'] == "M416") | (testkills['killed_by'] == "AUG") | (testkills['killed_by'] == "Groza") | (kills['killed_by'] == "M16A4") | (kills['killed_by'] == "SCAR-L"))]
killsS4 = testkills.loc[((testkills['killed_by'] == "Kar98k") | (testkills['killed_by'] == "AWM") | (testkills['killed_by'] == "M24"))]
killsS5 = testkills.loc[((testkills['killed_by'] == "UMP9") | (testkills['killed_by'] == "Micro UZI") | (testkills['killed_by'] == "Tommy Gun") | (testkills['killed_by'] == "Vector"))]
killsS6 = testkills.loc[((testkills['killed_by'] == "Mini 14") | (testkills['killed_by'] == "Mk14") | (testkills['killed_by'] == "SKS") | (testkills['killed_by'] == "VSS"))]
killsS7 = testkills.loc[(testkills['killed_by'] == "Grenade") & (testkills['kill_distance'] != 0.0)]

killsS0 = killsS0.reset_index(drop=True)
killsS1 = killsS1.reset_index(drop=True)
killsS2 = killsS2.reset_index(drop=True)
killsS3 = killsS3.reset_index(drop=True)
killsS4 = killsS4.reset_index(drop=True)
killsS5 = killsS5.reset_index(drop=True)
killsS6 = killsS6.reset_index(drop=True)
killsS7 = killsS7.reset_index(drop=True)

killsS0['weapon_predict'] = '0'
killsS1['weapon_predict'] = '0'
killsS2['weapon_predict'] = '0'
killsS3['weapon_predict'] = '0'
killsS4['weapon_predict'] = '0'
killsS5['weapon_predict'] = '0'
killsS6['weapon_predict'] = '0'
killsS7['weapon_predict'] = '0'
q = 0
z = 0
killsIND = [killsS0.index,killsS1.index,killsS2.index,killsS3.index,killsS4.index,killsS5.index,killsS6.index, killsS7.index]
for l in range(len(killsIND)):
    for ind in killsIND[l]:
        z += 1
        min = 9999999
        t = - 1
        for j in range(len(average)):
            if (abs(killsS3['kill_distance'][ind] - average[j]) < min):
                min = abs(killsS3['kill_distance'][ind] - average[j])
                t = j
        if t == l:
            q += 1

print("Accuracy : " + str(float(q) / z))
print("--- %s seconds ---" % (time.time() - start_time))
