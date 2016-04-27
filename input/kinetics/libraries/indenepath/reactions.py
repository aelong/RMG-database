#!/usr/bin/env python
# encoding: utf-8

name = "indenepath"
shortDesc = u"shamel's seed mech for CPD"
longDesc = u"""
This mechanism is pulled directly from the mechanism provided by professor greeen that was created by shamel
it is unkown where the data originates from
"""


# ! Reaction index: Chemkin #1; RMG #1
# ! Library reaction: indenepath
# ! Seed Mechanism: indenepath
# CPDyl(14)+CPD(1)=C10H11(15)                         2.830e+02 2.740     3.300
entry(
    index = 1,
    label = "CPDyl + CPD <=> C10H11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(2.830e+02, 'cm^3/(mol*s)'),
        n=2.740,
        Ea=(3.300, 'cal/mol'),
        T0=(1, 'K')),
)
# ! Reaction index: Chemkin #2; RMG #2
# ! Library reaction: indenepath
# ! Seed Mechanism: indenepath
# C10H11(15)=pdt15(16)                                1.120e+08 1.640     22.700
entry(
    index = 2,
    label = "C10H11 <=> pdt15",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(1.120e+08, 'cm^3/(mol*s)'),
        n=1.640,
        Ea=(22.700, 'cal/mol'),
        T0=(1, 'K')),
)
# ! Reaction index: Chemkin #3; RMG #3
# ! Library reaction: indenepath
# ! Seed Mechanism: indenepath
# pdt15(16)=pdt16(17)                                 5.290e+09 1.040     31.200
entry(
    index = 3,
    label = "pdt15 <=> pdt16",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(5.290e+09, 'cm^3/(mol*s)'),
        n=1.040,
        Ea=(31.200, 'cal/mol'),
        T0=(1, 'K')),
)
# ! Reaction index: Chemkin #4; RMG #4
# ! Library reaction: indenepath
# ! Seed Mechanism: indenepath
# pdt16(17)=pdt20(18)                                 2.590e+08 1.010     26.400
entry(
    index = 4,
    label = "pdt16 <=> pdt20",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(2.590e+08, 'cm^3/(mol*s)'),
        n=1.010,
        Ea=(26.400, 'cal/mol'),
        T0=(1, 'K')),
)
# ! Reaction index: Chemkin #5; RMG #5
# ! Library reaction: indenepath
# ! Seed Mechanism: indenepath
# pdt20(18)=pdt21(19)                                 7.900e+10 0.290     21.100
entry(
    index = 5,
    label = "pdt20 <=> pdt21",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(7.900e+10, 'cm^3/(mol*s)'),
        n=0.290,
        Ea=(21.100, 'cal/mol'),
        T0=(1, 'K')),
)
# ! Reaction index: Chemkin #6; RMG #6
# ! Library reaction: indenepath
# ! Seed Mechanism: indenepath
# pdt21(19)=pdt27(20)                                 6.070e+06 2.000     26.100
entry(
    index = 6,
    label = "pdt19 <=> pdt27",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(6.070e+06, 'cm^3/(mol*s)'),
        n=2.00,
        Ea=(26.100, 'cal/mol'),
        T0=(1, 'K')),
)
# ! Reaction index: Chemkin #7; RMG #7
# ! Library reaction: indenepath
# ! Seed Mechanism: indenepath
# pdt27(20)=INDENE(21)+CH3(22)                        1.710e+11 0.860     22.700
entry(
    index = 7,
    label = "pdt27 <=> INDENE + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(1.710e+11, 'cm^3/(mol*s)'),
        n=0.860,
        Ea=(22.700, 'cal/mol'),
        T0=(1, 'K')),
)
# ! Reaction index: Chemkin #8; RMG #8
# ! Library reaction: indenepath
# ! Seed Mechanism: indenepath
# C10H11(15)=pdt55(23)                                6.360e+06 1.700     31.700
entry(
    index = 8,
    label = "C10H11 <=> pdt55",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(6.360e+06, 'cm^3/(mol*s)'),
        n=1.700,
        Ea=(31.700, 'cal/mol'),
        T0=(1, 'K')),
)
# ! Reaction index: Chemkin #9; RMG #9
# ! Library reaction: indenepath
# ! Seed Mechanism: indenepath
# pdt15(16)=pdt55(23)                                 1.780e+06 1.750     25.300
entry(
    index = 9,
    label = "pdt15 <=> pdt55",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(1.780e+06, 'cm^3/(mol*s)'),
        n=1.750,
        Ea=(25.300, 'cal/mol'),
        T0=(1, 'K')),
)
# ! Reaction index: Chemkin #10; RMG #10
# ! Library reaction: indenepath
# ! Seed Mechanism: indenepath
# pdt55(23)=pdt58(24)                                 2.020e+11 0.790     35.300
entry(
    index = 10,
    label = "pdt15 <=> pdt55",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(2.020e+11, 'cm^3/(mol*s)'),
        n=0.790,
        Ea=(35.300, 'cal/mol'),
        T0=(1, 'K')),
)
# ! Reaction index: Chemkin #11; RMG #11
# ! Library reaction: indenepath
# ! Seed Mechanism: indenepath
# pdt58(24)=pdt20(18)                                 1.040e+07 1.610     27.100
entry(
    index = 11,
    label = "pdt15 <=> pdt55",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(2.020e+11, 'cm^3/(mol*s)'),
        n=0.790,
        Ea=(35.300, 'cal/mol'),
        T0=(1, 'K')),
)