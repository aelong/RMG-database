#!/usr/bin/env python
# encoding: utf-8

name = "aromatics_revised"
shortDesc = u"from shamel's aromatics_revised"
longDesc = u"""
created from same named library owned by shamel merchant on RMG JAVA
"""

entry(
	index = 1,
	label = "C5H5CH3_5 <=> C5H5CH3_1",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(7.03e8,'cm^3/(mol*s)'),
		n=1.2,
		Ea=(24.8,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 2,
	label = "C5H5CH3_1 <=> C5H5CH3_2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.65e7,'cm^3/(mol*s)'),
		n=2.1,
		Ea=(25.1,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 3,
	label = "CPDYL + METHYL <=> C5H5CH3_5",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(8.34e15,'cm^3/(mol*s)'),
		n=-0.7,
		Ea=(-0.5,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 4,
	label = "CPDYL + ETHYL <=> ethylCPD",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(8.34e15,'cm^3/(mol*s)'),
		n=-0.7,
		Ea=(-0.5,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 5,
	label = "MCPDYL + METHYL <=> 2MCPD",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(8.34e15,'cm^3/(mol*s)'),
		n=-0.7,
		Ea=(-0.5,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 6,
	label = "FULVENE + H2 <=> C5H5CH3_5",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.44e5,'cm^3/(mol*s)'),
		n=3.9,
		Ea=(81.1,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 7,
	label = "FULVENE + H2 <=> C5H5CH3_1",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(6.08e7,'cm^3/(mol*s)'),
		n=1.4,
		Ea=(71.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 8,
	label = "FULVENE + H2 <=> C5H5CH3_2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.62e7,'cm^3/(mol*s)'),
		n=1.6,
		Ea=(55.5,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 9,
	label = "MCPDYL + H <=> C5H5CH3_5",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(4.57e14,'cm^3/(mol*s)'),
		n=-0.1,
		Ea=(0.4,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 10,
	label = "MCPDYL + H <=> C5H5CH3_1",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(4.09e13,'cm^3/(mol*s)'),
		n=0.3,
		Ea=(0.1,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 11,
	label = "C5H5CH2-2 + H <=> C5H5CH3_1",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.05e12,'cm^3/(mol*s)'),
		n=0.6,
		Ea=(-0.2,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 12,
	label = "MCPDYL + H <=> C5H5CH3_2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(9.05e13,'cm^3/(mol*s)'),
		n=0.1,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 13,
	label = "C5H5CH2-3 + H <=> C5H5CH3_2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(3.43e12,'cm^3/(mol*s)'),
		n=0.5,
		Ea=(-0.1,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 14,
	label = "C5H5CH2-1 + H <=> C5H5CH3_5",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.10e12,'cm^3/(mol*s)'),
		n=0.6,
		Ea=(-0.8,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 15,
	label = "vinylfulvene + H <=> STYRENE + H",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.934e+51,'cm^3/(mol*s)'),
		n=-10.45,
		Ea=(28.65,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 16,
	label = "TOLUENE + HO2 <=> BENZYL + H2O2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(3.97e11,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(14.07,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 17,
	label = "CP <=> CPD + H2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.24e+13,'cm^3/(mol*s)'),
		n=0.00,
		Ea=(60.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 18,
	label = "C5H7VIN <=> C5H7_125p",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.0e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(33.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 19,
	label = "C5H7_125p <=> C2H4 + H2CCCH",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.0e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(22.5,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 20,
	label = "CH2CO + H <=> CH3CO",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.30e8,'cm^3/(mol*s)'),
		n=1.61,
		Ea=(2.63,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 21,
	label = "C4H3 + H <=> C4H2 + H2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(5.0e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 22,
	label = "C3H6 + O <=> ETHYL + HCO",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.58e7,'cm^3/(mol*s)'),
		n=1.76,
		Ea=(-1.216,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 23,
	label = "C3H4a + O <=> C2H4 + CO",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.34e7,'cm^3/(mol*s)'),
		n=1.88,
		Ea=(0.1790,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 24,
	label = "C3H2 + O2 <=> HCCO + CO + H",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(5.0e12,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 25,
	label = "C4H3 + O <=> CH2CO + C2H",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.0e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 26,
	label = "C4H3 + CH2 <=> C3H4a + C2H",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.0e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 27,
	label = "CH2(S) + C2H4 <=> ALLYL + H",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.3e14,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 28,
	label = "C2H3 + METHYL <=> ALLYL + H",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(4.73e2,'cm^3/(mol*s)'),
		n=3.7,
		Ea=(5.677,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 29,
	label = "C2H2 + C2H <=> C4H3",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(9.6358e16,'cm^3/(mol*s)'),
		n=-1.19575,
		Ea=(3.785,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 30,
	label = "CPDYL + O <=> BUTADIENYL + CO",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(3.2e13,'cm^3/(mol*s)'),
		n=-0.17,
		Ea=(0.440,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 31,
	label = "C2H3 + C2H2 <=> BUTADIENYL",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.14424e+23,'cm^3/(mol*s)'),
		n=-3.72699,
		Ea=(8.15962,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 32,
	label = "CPD <=> C5H6a",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.35e+15,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(80.450,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 33,
	label = "C5H6a <=> C3H4p + C2H2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.88e+13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(66.550,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 34,
	label = "CPD <=> C2H2 + C3H4a",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(3.80e+17,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(104.000,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 35,
	label = "CPD <=> C5H6b",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(8.50e+14,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(90.540,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 36,
	label = "C5H6b <=> C2H2 + C3H4a",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(3.55e+13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(63.360,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 37,
	label = "CPD + H2CCCH <=> CPDYL + C3H4p",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.10e+11,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(5.5,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 38,
	label = "C3H2lin + C2H2 <=> C5H4",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(6.68e4,'cm^3/(mol*s)'),
		n=2.45,
		Ea=(6.83,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 39,
	label = "C5H5new <=> C5H5orig",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.52e7,'cm^3/(mol*s)'),
		n=1.87,
		Ea=(55.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 40,
	label = "C5H5orig <=> CPDYL",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(5.82e6,'cm^3/(mol*s)'),
		n=1.88,
		Ea=(24.67,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 41,
	label = "C5H5new <=> C5H5newacyc",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(8.78e11,'cm^3/(mol*s)'),
		n=0.77,
		Ea=(33.44,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 42,
	label = "C5H5orig <=> CHCCH2CHCH",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(9.66e11,'cm^3/(mol*s)'),
		n=0.65,
		Ea=(42.43,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 43,
	label = "C5H5orig <=> C5H5origacycB",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(6.70e11,'cm^3/(mol*s)'),
		n=0.70,
		Ea=(41.82,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 44,
	label = "C3H4a + H <=> ALLYL",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(4.67385e+51,'cm^3/(mol*s)'),
		n=-11.45,
		Ea=(21.34,'kcal/mol'),
		T0=(1,'K'),
	),
)


# entry(
# 	index = 45,
# 	label = "C3H4a + H <=> ALLYL",
# 	degeneracy = 1,
# 	kinetics=Arrhenius(
# 		A=(3.31867e+30,'cm^3/(mol*s)'),
# 		n=-5.78,
# 		Ea=(6.913,'kcal/mol'),
# 		T0=(1,'K'),
# 	),
# )

entry(
	index = 46,
	label = "C3H4a + H <=> METHYL + C2H2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.26483e20,'cm^3/(mol*s)'),
		n=-1.83,
		Ea=(15.003,'kcal/mol'),
		T0=(1,'K'),
	),
)


# entry(
# 	index = 47,
# 	label = "C3H4a + H <=> METHYL + C2H2",
# 	degeneracy = 1,
# 	kinetics=Arrhenius(
# 		A=(12286.92,'cm^3/(mol*s)'),
# 		n=2.68,
# 		Ea=(6.335,'kcal/mol'),
# 		T0=(1,'K'),
# 	),
# )

entry(
	index = 48,
	label = "H + C2H <=> C2H2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.25e13,'cm^3/(mol*s)'),
		n=0.32,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 49,
	label = "H + H2CCCH <=> C3H4a",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(6.62e13,'cm^3/(mol*s)'),
		n=0.20600,
		Ea=(-0.17297,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 50,
	label = "H + ALLYL <=> C3H6",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.59e14,'cm^3/(mol*s)'),
		n=0.176,
		Ea=(-0.12511,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 51,
	label = "CPD + O <=> CPDYL + OH",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(4.8e4,'cm^3/(mol*s)'),
		n=2.70,
		Ea=(1.10,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 52,
	label = "CPD + H <=> CPDYL + H2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.09e7,'cm^3/(mol*s)'),
		n=2.21,
		Ea=(3.2,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 53,
	label = "CPD + OH <=> CPDYL + H2O",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(3.1e6,'cm^3/(mol*s)'),
		n=2.0,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 54,
	label = "CPD + HO2 <=> CPDYL + H2O2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.1e4,'cm^3/(mol*s)'),
		n=2.6,
		Ea=(12.9,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 55,
	label = "CPD + METHYL <=> CPDYL + CH4",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(3.0e11,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(5.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 56,
	label = "CPD + ALLYL <=> CPDYL + C3H6",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.10e11,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(5.5,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 57,
	label = "CPD + O2 <=> CPDYL + HO2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.4e12,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(31.6,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 58,
	label = "C3H4p + O <=> H2CCCH + OH",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(3.4e4,'cm^3/(mol*s)'),
		n=2.16,
		Ea=(4.8,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 59,
	label = "CPD + H <=> C5H7JAI",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.108e9,'cm^3/(mol*s)'),
		n=1.55,
		Ea=(2.28,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 60,
	label = "C5H7JAI <=> C5H7LIN",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(8.68e12,'cm^3/(mol*s)'),
		n=0.48,
		Ea=(43.11,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 61,
	label = "C5H7LIN <=> ALLYL + C2H2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(4.72e11,'cm^3/(mol*s)'),
		n=0.81,
		Ea=(24.35,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 62,
	label = "BENZENE + O <=> PHENOXY + H",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.8e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(4.9,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 63,
	label = "BENZENE + OH <=> PHENOL + H",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.3e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(10.6,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 64,
	label = "BENZENE + O <=> PHENYL + OH",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.0e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(14.7,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 65,
	label = "BENZENE + HO2 <=> PHENYL + H2O2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(5.5e12,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(28.9,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 66,
	label = "BENZENE + METHYL <=> PHENYL + CH4",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.0e12,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(15.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 67,
	label = "BENZENE + ETHYL <=> PHENYL + C2H6",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(6.3e11,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(15.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 68,
	label = "BENZENE + ALLYL <=> PHENYL + C3H6",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(6.3e11,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(20.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 69,
	label = "BENZENE + BUTADIENYL <=> PHENYL + BD",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(6.3e11,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(15.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 70,
	label = "BENZENE + BD2YL <=> PHENYL + BD",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(6.3e11,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(20.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 71,
	label = "PHENYL + O2 <=> PHENOXY + O",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.6e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(6.1,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 72,
	label = "PHENYL + O <=> CPDYL + CO",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.0e14,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 73,
	label = "PHENYL + OH <=> PHENOL",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.0e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 74,
	label = "PHENYL + HO2 <=> PHENOXY + OH",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(5.0e12,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 75,
	label = "PHENOXY <=> CO + CPDYL",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.5e11,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(43.8,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 76,
	label = "PHENOXY + H <=> CPD + CO",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.1e53,'cm^3/(mol*s)'),
		n=-10.7,
		Ea=(41.4,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 77,
	label = "PHENOXY + O <=> CPDYL + CO2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.0e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 78,
	label = "PHENOL <=> CPD + CO",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.0e12,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(61.2,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 79,
	label = "PHENOL + O2 <=> HO2 + PHENOXY",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.0e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(38.8,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 80,
	label = "PHENOL + H <=> PHENOXY + H2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.2e14,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(12.4,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 81,
	label = "PHENOL + O <=> PHENOXY + OH",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.3e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(2.9,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 82,
	label = "PHENOL + OH <=> PHENOXY + H2O",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.4e8,'cm^3/(mol*s)'),
		n=1.4,
		Ea=(-0.96,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 83,
	label = "PHENOL + HO2 <=> PHENOXY + H2O2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.0e12,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(10.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 84,
	label = "PHENOL + METHYL <=> PHENOXY + CH4",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.8e11,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(7.7,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 85,
	label = "PHENOL + PHENYL <=> PHENOXY + BENZENE",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(4.9e12,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(4.4,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 86,
	label = "PHENOL + CPDYL <=> PHENOXY + CPD",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(4.9e11,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(9.4,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 87,
	label = "PHENOL + ALLYL <=> PHENOXY + C3H6",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(4.9e11,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(9.4,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 88,
	label = "PHENOL + BD2YL <=> PHENOXY + BD",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(4.9e11,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(9.4,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 89,
	label = "PHENYL + H2 <=> BENZENE + H",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(5.7e4,'cm^3/(mol*s)'),
		n=2.43,
		Ea=(6.2800,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 90,
	label = "PHENYL + OH <=> BENZYNE + H2O",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(1.0e07,'cm^3/(mol*s)'),
		n=2.00,
		Ea=(1.000,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 91,
	label = "PHENYL + OH <=> PHENOXY + H",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(5.0e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 92,
	label = "PHENOL + C2H3 <=> PHENOXY + C2H4",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(6.0e12,'cm^3/(mol*s)'),
		n=0.00,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 93,
	label = "PHENYL + H <=> BENZYNE + H2",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(2.0e07,'cm^3/(mol*s)'),
		n=2.00,
		Ea=(1.000,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 94,
	label = "C3H2 + HCCO <=> C4H3b + CO",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(3.0e13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 95,
	label = "C3H2 + OH <=> C2H2 + HCO",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(5.00e+13,'cm^3/(mol*s)'),
		n=0.0,
		Ea=(0.0,'kcal/mol'),
		T0=(1,'K'),
	),
)

entry(
	index = 96,
	label = "H2CCCH + H2CCCH <=> BENZENE",
	degeneracy = 1,
	kinetics=Arrhenius(
		A=(3.160e+55,'cm^3/(mol*s)'),
		n=-12.55,
		Ea=(22.26,'kcal/mol'),
		T0=(1,'K'),
	),
)


