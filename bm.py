#Realización de los cálculos de balance 
from const import *
from inputs import *

def water_flow():
    #invocar peticiones de usuario para hacer los cálculos
    p_elec, eta_elec = peticiones()

    #cálculo de la energía útil 
    e_util = p_elec*(eta_elec/100)

    #cálculo de los moles de H2 que se producen con esa energía electrica
    n_h2 = e_util/lhv               #mol/s

    #definición de los moles de H2O
    n_h2o = n_h2                    #Por estequiometría 1 mol de H2O --> 1 mol de H2

    #cálculo de la masa de agua necesaria estequiométrica
    m_h2o = n_h2o*M_h2o*3.6         #Masa de agua en kg/h 

    