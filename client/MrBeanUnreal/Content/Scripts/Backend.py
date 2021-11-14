import unreal_engine as ue
import random
from QuSym import *

import numpy as np
from numpy import pi

def init_circ(n):
    circ = QuantumCircuit(n)
    return circ

def get_sv(circ):
    statevector = circ.statevector()
    return statevector

def get_prob(circ):
    P = circ.get_counts()
    return P

def arraystring(v):
    L = []
    for i in v:
        x = round(i, 3)
        L.append(str(x))
    return L

def set_circuit_measure(sv, circ):
    circ.reset(0)
    circ.reset(1)
    prob = abs(sv)**2
    
    if prob[1] == 1:
        circ.x(0)
        
    elif prob[2] == 1:
        circ.x(1)
        
    elif prob[3] == 1:
        circ.x(0)
        circ.x(1)
    
    return circ

class QLogic:

    def begin_play(self):
        self.actor = self.uobject.get_owner()
        self.circ = init_circ(2)

        self.X0()
        self.get_probv()
        
    def init(self):
        self.circ = init_circ(2)
        self.X0()
        
    def collapse(self):
        self.circ.collapse_all()
        return self.circ
         
    def get_probv(self):
        P = get_prob(self.circ)
        #ue.print_string(str(P))
        return P

    def reset0(self):
        self.circ.reset(0)
        return self.circ
    
    def reset1(self):
        self.circ.reset(0)
        return self.circ

    def X0(self):
        self.circ.x(0)
        return self.circ

    def H0(self):
        self.circ.h(0)
        return self.circ

    def Y0(self):
        self.circ.y(0)
        return self.circ

    def Z0(self):
        self.circ.z(0)
        return self.circ

    def S0(self):
        self.circ.s(0)
        return self.circ

    def CNOT0(self):
        self.circ.cx(0, 1)
        return self.circ
    
    def X1(self):
        self.circ.x(1)
        return self.circ

    def H1(self):
        self.circ.h(1)
        return self.circ

    def Y1(self):
        self.circ.y(1)
        return self.circ

    def Z1(self):
        self.circ.z(1)
        return self.circ

    def S1(self):
        self.circ.s(1)
        return self.circ

    def CNOT1(self):
        self.circ.cx(1, 0)
        return self.circ




        