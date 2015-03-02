#!/usr/bin/python2

import ephem

class Tracker(object):
    """Class to track a single object"""

    def _process_file(self):
        """Matches the name and returns the next two lines in the TLE
        data set"""
        try:
            f = open(self.TLE_set, "r")
        except IOError:
            print "Error in opening TLE_set file -- did you run get_stations.sh?"

        with f:
            for line in f:
                if line.rstrip("\n") == self.obj_name:
                    matched_lines = [f.next().rstrip("\n") for i in range(2)]
                    return matched_lines
            else:
                raise Exception("Error in reading TLE_set file: " +
                        self.obj_name + " was not found")

    def _print_debug_get_info_object(self):
        print "** debug data: **"
        print "Object name: " + self.obj_name
        print "TLE Data: " + "\n".join(self._process_file())
        print "** end of debug data **"

    def calculate_current_position(self):
        """Returns the current position for our CubeSat"""
        # set the time and calculate position
        self.our_position.date = ephem.now()
        self.our_cubesat.compute(self.our_position)
        return (self.our_cubesat.alt, self.our_cubesat.az)

    def calculate_next_position(self):
        self.our_position.date = ephem.now()
        return self.our_position.next_pass(self.our_cubesat)

    def __init__(self, textfile = "stations.txt", name = "ISS (ZARYA)",
        # roof of TSH, (longitude, latitude)
        position = ('43.26427', '-79.91766')):
        """Sets tracking object properties"""

        self.TLE_set  = textfile
        self.obj_name = name # our satellite name

        # create ephem observer
        self.our_position = ephem.Observer()
        self.our_position.lat, self.our_position.lon = position
        # 75m, plus 25 for building height
        self.our_position.elevation = 100

        # take the input "stations.txt" and find our object in the file
        self.line1, self.line2 = self._process_file()

        # create ephem object, and send it the processed TLE data
        self.our_cubesat = ephem.readtle(name, self.line1, self.line2)


