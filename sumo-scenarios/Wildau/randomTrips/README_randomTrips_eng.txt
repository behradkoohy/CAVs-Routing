randomTrips

SUMO has the tool randomTrips, which randomly generates routes within a network. The whole thing is called in a batch file ("randomTrips.bat").
Inland and transit traffic can be weighted using the fringe factor. Ever higher the number is more transit traffic will be generated.
"P" stands for the period which indicates how often vehicles are "created". Ever smaller the period is  more vehicles are produced.
The two factors can be adjusted until the simulation appears realistic.

Based on Wildau, three methods were used for random trips.
In the first step, the raw route file was run through by the WebWizard ("osm. passtger.rou.xml"), where by the standard settings of the fringe factor and the period were adopted.
In the second step, the fringe factor and the period were changed in order to obtain the desired appearance (fringe factor = 7, period = 1,850).
A further step is the application of the function --speed-exponent, whereby edges with a higher speed have a higher probability of being traveled on.

An output file can then be created, where by the routes generated by the tool must be specified as a route file.