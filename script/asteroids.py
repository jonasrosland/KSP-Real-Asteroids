# Created by Jonas Rosland, @jonasrosland

import csv
import json
import math

asteroids = list(csv.DictReader(open('asteroids.csv', 'rb')))

for line in asteroids:
    designation = line["pdes"]
    name = line["name"]
    magnitude = line["H"]
    # In km
    diameter = line["diameter"]
    albedo = line["albedo"]
    # In hours
    rotation = line["rot_per"]
    eccentricity = line["e"]
    semimajoraxis = line["a"]
    inclination = line["i"]
    longitudeofascendingnode = line["om"]
    argumentofperihelion = line["w"]
    meananomaly = line["ma"]

    semimajoraxis = str(13599840256 * float(semimajoraxis))
    # Calculating volumes as spherical objects to make it easy
    volume = (math.pi * pow(float(diameter), 3))/6
    mass = str(volume * 2)
    radius = str(float(diameter)/2)
    geeASL = str(6.667197e-11 * float(mass) / pow(float(radius), 2))

    f = open(name+".cfg", 'w')

    f.write("@Kopernicus:AFTER[KOPERNICUS]\n{\n    Body\n    {\n")
    f.write("        name = " + name + "\n" + "        flightGlobalsIndex = 1000" + designation + "\n")
    f.write("        Properties\n        {\n")
    f.write("            description = " + "Awesome asteroid!\n")
    f.write("            radius = " + radius + "\n")
    f.write("            mass = " + mass + "\n")
    f.write("            geeASL = " + geeASL + "\n")
    f.write("        }" + "\n")
    f.write("        {" + "\n")
    f.write("            referenceBody = Sun" + "\n")
    f.write("            color = 1,1,0,1" + "\n")
    f.write("            inclination = " + inclination + "\n")
    f.write("            eccentricity = " + eccentricity + "\n")
    f.write("            semiMajorAxis = " + semimajoraxis + "\n")
    f.write("            longitudeOfAscendingNode = " + longitudeofascendingnode + "\n")
    f.write("            argumentOfPeriapsis = " + argumentofperihelion + "\n")
    f.write("            meanAnomalyAtEpoch = " + meananomaly + "\n")
    f.write("            epoch = 0" + "\n")
    f.write("         }" + "\n")
    f.write("     }" + "\n")
    f.write("}" + "\n")


    f.close
