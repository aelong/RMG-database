#!/usr/bin/env python
# encoding: utf-8

name = "CPD_seed"
shortDesc = u"Cyclopentadiene pyrolysis in the presence of ethene"
longDesc = u"""
Created: 4/27/16 by Alan Long

For: attempting to improve mechanism by Shamel merchant.
"""
entry(
    index = 1,
    label = "CPD + C2H4 <=> ethylCPDa",
    degeneracy = 1,
    kinetics=Arrhenius(
        A=(0.194145, 'cm^3/(mol*s)'),
        n=3.46783,
        Ea=(25.68, 'kcal/mol'),
        T0=(1, 'K'),
        Tmin=(303.03, 'K'),
        Tmax=(2500, 'K'),
        comment='Fitted to 59 data points; dA = *|/ 1.06471, dn = +|- 0.00822885, dEa = +|- 0.0452669 kJ/mol',
    ),
)

#-----H radical formation-----


#A: From shamel mech
# ! Reaction index: Chemkin #767; RMG #767
# ! Template reaction: R_Recombination
# ! R_Recombination exact:   [ C_rad/H2/Cs , H_rad ]
# addB(35)+H(29)=C7H10(144)                           1.000e+14 0.000     0.000

entry(
    index = 2,
    label = "H + ethylCPD_radE <=> ethylCPDa",
    degeneracy = 1,
    kinetics=Arrhenius(
        A=(1e+14, 'cm^3/(mol*s)'),
        n=0.000,
        Ea=(0.000, 'kcal/mol'),
        T0=(1, 'K'),
        comment='',
    ),
)

# ! Reaction index: Chemkin #811; RMG #811
# ! Template reaction: R_Recombination
# ! R_Recombination estimate: (Average:)  [ C_rad/Cs , H_rad ]
# C7H9(75)+H(29)=C7H10(144)    2.920e+13 0.180     0.124

entry(
    index = 3,
    label = "H + ethylCPD_radJ <=> ethylCPDa",
    degeneracy = 1,
    kinetics=Arrhenius(
        A=(2.920e+13, 'cm^3/(mol*s)'),
        n=0.180,
        Ea=(0.124, 'kcal/mol'),
        T0=(1, 'K'),
        comment='',
    ),
)

#A: using the cpdyl formation rxn from shamel mech
# ! Reaction index: Chemkin #37; RMG #37
# ! Template reaction: R_Recombination
# ! R_Recombination exact:   [ C_rad_cyclopentadiene , H_rad ]
# CPDyl(14)+H(29)=CPD(1)                              2.600e+14 0.000     0.000

entry(
    index = 7,
    label = "H + ethylCPDb_rad <=> ethylCPDb",
    degeneracy = 1,
    kinetics=Arrhenius(
        A=(2.60e+14, 'cm^3/(mol*s)'),
        n=0.180,
        Ea=(0.124, 'kcal/mol'),
        T0=(1, 'K'),
        comment='',
    ),
)

entry(
    index = 8,
    label = "H + ethylCPDc_rad <=> ethylCPDc",
    degeneracy = 1,
    kinetics=Arrhenius(
        A=(2.6e+14, 'cm^3/(mol*s)'),
        n=0.180,
        Ea=(0.124, 'kcal/mol'),
        T0=(1, 'K'),
        comment='',
    ),
)

#------ Methyl Radical Formation ------

# ! Reaction index: Chemkin #820; RMG #820
# ! Template reaction: R_Recombination
# ! R_Recombination exact:   [ C_rad/H2/Cs , C_methyl ]
# C6H7(121)+CH3(22)=C7H10(144)                        3.370e+13 0.000     0.000

entry(
    index = 4,
    label = "CH3 + CH2CPD <=> ethylCPDa",
    degeneracy = 1,
    kinetics=Arrhenius(
        A=(3.370e+13, 'cm^3/(mol*s)'),
        n=0.000,
        Ea=(0.000, 'kcal/mol'),
        T0=(1, 'K'),
        comment='',
    ),
)

#----- Hydrogen Shifts -----

# ! Reaction index: Chemkin #896; RMG #896
# ! Template reaction: H_shift_cyclopentadiene
# ! H_shift_cyclopentadiene exact:   [ cyclopentadiene ]
# C7H10(144)=C7H10(145)                               1.012e+08 1.740     24.300



entry(
    index=5,
    label="ethylCPDa <=> ethylCPDb",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.012e+08, 'cm^3/(mol*s)'),
        n=1.740,
        Ea=(24.300, 'kcal/mol'),
        T0=(1, 'K'),
        comment='',
    ),
)

#A: copy of A->B above

entry(
    index = 6,
    label = "ethylCPDb <=> ethylCPDc",
    degeneracy = 1,
    kinetics=Arrhenius(
        A=(1.012e+08, 'cm^3/(mol*s)'),
        n=1.740,
        Ea=(24.300, 'kcal/mol'),
        T0=(1, 'K'),
        comment='',
    ),
)