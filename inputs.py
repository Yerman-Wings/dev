#Peticiones a usuario de variables 

def peticiones():
    #solicitud de la potencia eléctrica del electrolizador 
    p_elec = input('¿De que potencia es el electrolizador?\nIntroduce el valor en kW:')
    #solicitud de la eficiencia electrica del electrolizador
    eta_elec = input('¿Cual es la eficiencia eléctrica del electrolziador?\nIntroduce el valor en %:')

    return p_elec, eta_elec