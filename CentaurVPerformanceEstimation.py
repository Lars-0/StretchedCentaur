import math
#fundamental constants
SteelDensity = 7800 # kg / m^3
H_Density = 72 # kg / m^3
O_Density = 1146 # kg / m^3
g = 9.81 # m/s^2
pi = 3.14159

#Parameters to adjust
Diameter = 3.05 # meters
Thickness = .030 * 24.5 / 1000 # inches-to-meters
M_Ratio = 5.88 #unitless
Payload = 28790 #kg
Delta_V = 3000 # m/s
ISP = 425 # Seconds, estimate for BE-3U
EngineMass = 200 # kg, Estimate for BE-3U
StageMass = 2247 - 168 #estimate for tank minus RL-10B
InitialLength = 12.68-2.32 # meters, total length minus engine length
Thrust = 670 # KN, wikipedia, not used in estimates
PropMass = 20830 # kg


# Basic calculations
AvgDensity = H_Density*(1-1/5.88)+O_Density*(1/5.88) # kg / m^3

Area = math.pow((Diameter - (Thickness * 2)),2) * pi / 4 # m^2
print Area
SpecificPropLoad = AvgDensity*Area # kg / m
SpecificTankMass = pi*Diameter*Thickness*SteelDensity # kg / m
print SpecificPropLoad
print SpecificTankMass
Prop_Tank_Ratio = SpecificPropLoad / SpecificTankMass # unitless 
DryMass = Payload + StageMass # Stage mass of Cantaur IV.

#The Meat
Equation_Left =  math.exp(Delta_V / (g * ISP))
ExtraTankMass = (DryMass * Equation_Left -(DryMass + PropMass)) / (1 + Prop_Tank_Ratio - Equation_Left)
Extra_length = ExtraTankMass / SpecificTankMass
Extra_prop = Extra_length * SpecificPropLoad
Total_length = InitialLength + Extra_length

#determining the split line between H2 and O2
BulkheadVolume = Diameter/3 * Diameter* Diameter * pi * .667 #Assuming 3:1 ratio bulkheads and endcaps
TotalVolume = Area * (Total_length) 
HydrogenMass = (PropMass+Extra_prop) * (1/ M_Ratio)
HydrogenVolume = HydrogenMass / H_Density
HydrogenVolumeWithoutCaps = HydrogenVolume - BulkheadVolume + (Area*Diameter*Diameter/3)
HydrogenLength = HydrogenVolumeWithoutCaps / Area

# Print Statements:
print "Extra Tank Mass: ",ExtraTankMass, "kg"
print "Extra tank length of : ", Extra_length, "meters"
print "Extra prop load: ", Extra_prop, "kg"
print "Total tank Length: ",Total_length, "meters"
print "Length of Hydrogen Section: ", HydrogenLength, "m"
