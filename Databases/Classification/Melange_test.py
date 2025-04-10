""" Modules """
import numpy as np
import random


""" 
***PARAMETRES***
- cristal_a (string) : name for one cristal of mix
- cristal_b (string) : name for one cristal of mix
- a_max,b_max (int) : number of diffractogramme generate for each cristal, default =1
- Percent (boolean) : if True we choose the percent of each cristal, else random
- percent_a/ percent_b (0 < float < 1)_if Percent=True: percent of each cristal (0.5 by default)
- numero : Pour le nom du fichier
"""

def melange(cristal_a,cristal_b,numero,a_max=1,b_max=1,Percent=False,percent_a = 0.5,percent_b = 0.5):
    
    Cristal_a = cristal_a
    Cristal_b = cristal_b
    a = 1
    b = 1
    
    
    #Si l'on a plus d'un diffractogramme de chaque type, on tire le numéro du diffractogramme des classes a et b que l'on tire
    if (a_max != 1 and b_max != 1):
    
        a_max = a_max
        b_max = b_max
        a = np.random.randint(a_max)+1
        b = np.random.randint(b_max)+1
        if (a == 0):
            a = 1
        if (b == 0):
            b = 1
    
    
    #Condition si dans la classe inconnu car mélange d'Halite et de Gibbsite
    """if (Cristal_a == 'Inconnu'):
        a_max = 300
        a = np.random.randint(a_max)
        Cristal_a = random.choice(['Calcite','Gibbsite'])
        if (a == 0):
            a = 1
    
    if (Cristal_b == 'Inconnu'):
        b_max = 300
        b = np.random.randint(b_max)
        Cristal_b = random.choice(['Calcite','Gibbsite'])   
        if (b == 0):
            b = 1
    """
    if (Percent == False):
        percent_cristal_a = np.random.rand()
        percent_cristal_a = round(percent_cristal_a,ndigits=2)
        percent_cristal_b = 1 - percent_cristal_a
    
    else : 
        percent_cristal_a = percent_a
        percent_cristal_b = percent_b
    
    cristal_a = open(Cristal_a+str(a)+'.txt', mode='r')
    cristal_b = open(Cristal_b+str(b)+'.txt', mode='r')
    melange = open('Melange'+str(numero)+'.txt',mode='w') 


    Intensity_a = np.zeros(2905)
    i = 0
    for line in cristal_a :
        if ('a' in line):
            titre_a = line
            melange.write(str(100*percent_cristal_a)+'% '+Cristal_a+' :'+ titre_a)
            continue
        Intensity_a[i] = float(line)
        i = i + 1

    Intensity_b = np.zeros(2905)
    i = 0
    for line in cristal_b :
        if ('a' in line):
            titre_b = line
            melange.write(str(100*percent_cristal_b)+'% '+Cristal_b+' :'+ titre_b)
            continue
        Intensity_b[i] = float(line)
        i = i + 1

    Intensity = np.zeros(2905)
    Intensity = (percent_cristal_a*Intensity_a)+(percent_cristal_b*Intensity_b)
        
    for i in range(len(Intensity)):
        melange.write(str(Intensity[i]) + '\n')
        
        

#On tire aléatoirement 2 composants parmi notre liste de 4 pour faire le mélange de classe
fichier = open('label_melange_test.csv',mode='w')



for i in range(300):
    composant = random.sample(['Calcite','Gibbsite','Dolomite','Hematite'],2) 
    percent_a = np.random.rand()
    percent_a = round(percent_a,ndigits=2)
    percent_b = 1 - percent_a
    percent_b = round(percent_b,ndigits=2)
    fichier.write('Melange'+str(i+701)+'.txt'+',') #Nom du fichier dans le label
    #Pour rédiger des pourcentages
    #Format : 'MelangeX.txt,%Calcite,%Gibbsite,%Dolomite,%Hematite'
    if (composant[0] == 'Calcite'):
        fichier.write(str(percent_a)+',')
    elif (composant[1] == 'Calcite'):
        fichier.write(str(percent_b)+',')
    else : 
        fichier.write('0'+',')
    
    if (composant[0] == 'Gibbsite'):
        fichier.write(str(percent_a)+',')
    elif (composant[1] == 'Gibbsite'):
        fichier.write(str(percent_b)+',')
    else : 
        fichier.write('0'+',')
        
    if (composant[0] == 'Dolomite'):
        fichier.write(str(percent_a)+',')
    elif (composant[1] == 'Dolomite'):
        fichier.write(str(percent_b)+',')
    else : 
        fichier.write('0'+',')
     
    
    if (composant[0] == 'Hematite'):
        fichier.write(str(percent_a))
    elif (composant[1] == 'Hematite'):
        fichier.write(str(percent_b))
    else : 
        fichier.write('0')
    melange(composant[0],composant[1],numero=i+701,a_max=400,b_max=400,Percent=True,percent_a=percent_a,percent_b=percent_b) #Création du fichier
    fichier.write('\n')

