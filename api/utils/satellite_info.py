# Import libraries
from tletools import TLE
import requests


data = requests.get('https://tle-backend.herokuapp.com/tlebyname/CARTOSAT-3/').json()

tle_lines = [ data["name"],data["line1"],data["line2"]]


tle = TLE.from_lines(*tle_lines) # generate TLE object with tle-tools library
orb = tle.to_orbit()


semimajor_axis = orb.a
orbit_period = orb.period
eccentricity = orb.ecc
argument_of_perigree = orb.argp
inclination = orb.inc
mean_motion = orb.n
eccentricity_vector = orb.e_vec
true_anomaly = orb.nu
raan = orb.raan
epoch = orb.epoch
argument_of_latitude = orb.arglat

