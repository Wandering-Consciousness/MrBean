import numpy as np
import random
#from sympy import *
import sympy as sp
from sympy.physics.quantum.qubit import Qubit
import sympy.physics.quantum.gate as spg
from sympy.physics.quantum.gate import CNOT, SWAP, CGate, IdentityGate, Gate, UGate
from sympy.physics.quantum.qapply import qapply
from sympy.parsing.sympy_parser import parse_expr
from sympy.physics.quantum.dagger import Dagger
from sympy.physics.quantum.state import Wavefunction
from sympy import Symbol, ImmutableMatrix

def separate_state(state):
    c = 0
    state = str(state)
    for i in range(len(state)):
        s = state[i]
        if s == '|':
            c = i
    if c == 0:
        coeff = 1
        
    else:
        coeff = state[0:c-1]
        coeff = parse_expr(coeff)
    pure_state = state[c:]
    return coeff, pure_state

def remove_ket(state_og):
    return state_og[1:-1]

def pure_to_string(state):
    s = '|'
    q = state.qubit_values
    for i in q:
        s += str(i)
    s += '>'
    return s

def modify_str(string, index, new):
    s = ''
    for i in range(len(string)):
        if (i != index) and (i != (len(string)+index)):
            g = string[i]
        else:
            g = str(new)
        s += g
    return s

def U3M(theta, phi, lamb):
    return ImmutableMatrix([[sp.cos(theta/2), -sp.exp(sp.I*lamb) * sp.sin(theta/2)],
                            [sp.exp(sp.I*phi) * sp.sin(theta/2), sp.exp(sp.I*(phi + lamb)) * sp.cos(theta/2)]])
    
def U3(qubit, theta, phi, lamb):
    return UGate((qubit,), U3M(theta, phi, lamb))

sqrt2i = 1/sp.sqrt(2)

iswapm = [[1, 0, 0, 0],
          [0, 0, sp.I, 0],
          [0, sp.I, 0, 0],
          [0, 0, 0, 1]]

sqrt_iswap = [[1, 0, 0, 0],
              [0, sqrt2i, sqrt2i*sp.I, 0],
              [0, sqrt2i*sp.I, sqrt2i, 0],
              [0, 0, 0, 1]]

sqrt_iswapH = [[1, 0, 0, 0],
              [0, sqrt2i, -sqrt2i*sp.I, 0],
              [0, -sqrt2i*sp.I, sqrt2i, 0],
              [0, 0, 0, 1]]

sqrt_swap = [[1, 0, 0, 0],
             [0, (1+sp.I)/2, (1-sp.I)/2, 0],
             [0, (1-sp.I)/2, (1+sp.I)/2, 0],
             [0, 0, 0, 1]]

def iswapM():
    return ImmutableMatrix(iswapm)

def sq_IswapM():
    return ImmutableMatrix(sqrt_iswap)

def sq_iswapHM():
    return ImmutableMatrix(sqrt_iswapH)

def sq_swapM():
    return ImmutableMatrix(sqrt_swap)

def Iswap(q1, q2):
    return UGate((q1, q2,), iswapM())

def sq_Iswap(q1, q2):
    return UGate((q1, q2,), sq_IswapM())

def sq_IswapH(q1, q2):
    return UGate((q1, q2,), sq_iswapHM())

def sq_swap(q1, q2):
    return UGate((q1, q2,), sq_swapM())

class QuantumCircuit:

    def __init__(self, n):
        self.num_qubits = n
        self.state = Qubit(("0"*n))
        
    def get_state(self):
        return self.state
    
    def x(self, qubit):
        self.state = qapply(spg.X(qubit)*self.state)

    def y(self, qubit):
        self.state = qapply(spg.Y(qubit)*self.state)

    def z(self, qubit):
        self.state = qapply(spg.Z(qubit)*self.state)

    def h(self, qubit):
        self.state = qapply(spg.H(qubit)*self.state)

    def s(self, qubit):
        self.state = qapply(spg.S(qubit)*self.state)

    def t(self, qubit):
        self.state = qapply(spg.T(qubit)*self.state)

    def cx(self, qubit1, qubit2):
        self.state = qapply(CNOT(qubit1, qubit2)*self.state)

    def swap(self, qubit1, qubit2):
        self.state = qapply(SWAP(qubit1, qubit2)*self.state)

    def iswap(self, qubit1, qubit2):
        self.state = qapply(Iswap(qubit1, qubit2)*self.state)

    def ccx(self, q1, q2, q3):
        self.state = qapply(CGate((q1, q2), spg.X(q3))*self.state)
        
    def U3(self, qubit, theta, phi, lamb):
        U = U3(qubit, theta, phi, lamb)
        self.state = qapply(U*self.state)
        
    def reset(self, qubit, set1 = 0):
        C = self.get_coeff()
        S = 0
        for element in C:
            bits = element[0][1:-1]
            bits = modify_str(bits, -(qubit+1), str(set1))
            S += element[1] * Qubit(bits)
            
        N = qapply(Dagger(S)*S).doit()
        self.state = qapply(S/sp.sqrt(N))
        
    def sqswap(self, q1, q2):
        self.state = qapply(sq_swap(q1, q2)*self.state)

    def sqiswap(self, q1, q2):
        self.state = qapply(sq_Iswap(q1, q2)*self.state)
        
    def sqiswapH(self, q1, q2):
        self.state = qapply(sq_IswapH(q1, q2)*self.state)

    def get_coeff(self):

        if type(self.state) is Qubit:
            Amp = []
            dagger_state = Dagger(self.state)
            coeff = dagger_state*self.state
            coeff = coeff.doit()
            pure_state = pure_to_string(self.state)
            Amp.append([pure_state, coeff])

        else:
            Amp = []
            d =  self.state._sorted_args
            for term in d:
                term_separated = term.as_coeff_Mul()
                coeff = term_separated[0]
                impure = term_separated[1]
                pure_state = separate_state(impure)
                coeff = coeff*pure_state[0]
                pure_state = pure_state[1]
                Amp.append([pure_state, coeff])
        
        return Amp
    
    def statevector(self):
        Amp = self.get_coeff()
        for count in Amp:
            count[0] = remove_ket(count[0])
        P = {}
        for count in Amp:
            if count[0]:
                P[count[0]] = (count[1]).evalf()
        return P

    def get_counts(self):
        Amp = self.get_coeff()
        for count in Amp:
            count[0] = remove_ket(count[0])
        P = {}
        for count in Amp:
            if count[0]:
                P[count[0]] = (sp.Abs(count[1])**2).evalf()
        return P

    def measurement(self):
        counts = self.get_counts()
        P = []
        for bit, shots in counts.items():
            x = [bit, shots]
            P.append(x)
        Q = np.transpose(np.array(P))
        list_of_candidates = Q[0]
        probability_distribution = Q[1]
        
        draw = random.choices(population = list_of_candidates, weights=probability_distribution)
        a = np.where(Q[0]==draw)[0][0]
        return P[a]

    def collapse_all(self):
        X = self.measurement()
        State = X[0]
        self.state = Qubit(State)
        return State
    
    def collapse(self, qubit):
        X = self.measurement() 
        state = X[0]
        bit_num = int(state[-(qubit+1)])    

        C = self.get_coeff()
        S = 0
        for element in C:
            bits = element[0][1:-1]
            if int(bits[-(qubit+1)]) == bit_num:
                S += element[1] * Qubit(bits)

        N = qapply(Dagger(S)*S)

        self.state = qapply(S/sp.sqrt(N))
        return bit_num