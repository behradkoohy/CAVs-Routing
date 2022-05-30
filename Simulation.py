import os
import sys

if "SUMO_HOME" in os.environ:
    tools = os.path.join(os.environ["SUMO_HOME"], "tools")
    sys.path.append(tools)
else:
    sys.exit("Please set SUMO_HOME")
import sumolib
import traci
from progress.bar import Bar

"""
simulation.py
This class handles the step by step running of the simulation
"""


class Simulation:
    def __init__(
        self,
        run_name,
        map_name=None,
        net=None,
        conf=None,
        route=None,
        end_time=3600,
        step_length=10,
        gui=False,
        progress_bar=True,
        trial_number=1,
        log_dir=None,
    ):
        self.run_name = run_name
        self.map_name = map_name
        self.net = net
        self.conf = conf
        self.trial_number = trial_number
        self.connection_name = str("-".join([run_name, "tr" + str(self.trial_number)]))
        self.route = route
        self.log_dir = log_dir

        if (self.net is None and self.route is None) and (self.conf is None):
            raise Exception("Either (Rou andNet) or (Sumocfg needed)")
        elif self.conf is not None:
            print("Using provided CONF", self.conf)
        elif net is None and route is None:
            print("Using provided Net/Rou", self.net, self.route)

        self.end_time = end_time
        self.step_length = step_length
        self.gui = gui
        # If we have no traffic data, use generated data
        if self.route is not None:
            sumo_cmd = [sumolib.checkBinary("sumo"), "-n", self.net, "-r", self.route]
        else:
            sumo_cmd = [
                sumolib.checkBinary("sumo"),
                "-c",
                self.conf,
            ]

        sumo_cmd += ["--random", "--time-to-teleport", "-1"]

        if self.log_dir is None:
            print(
                "No Log Directory specified; result-less run (usually done for debug purposes)"
            )
        else:
            if not os.path.exists(log_dir + self.connection_name):
                os.makedirs(log_dir + self.connection_name)
            sumo_cmd += [
                "--tripinfo-output",
                self.log_dir
                + self.connection_name
                + os.sep
                + "tripinfo_"
                + str(self.trial_number)
                + ".xml",
                "--tripinfo-output.write-unfinished",
                "--no-step-log",
                "True",
                "--no-warnings",
                "True",
                "--device.emissions.probability",
                "1.0",
            ]

        # Start SUMO
        traci.start(sumo_cmd, label=self.connection_name)
        self.sumo = traci.getConnection(self.connection_name)


        exit()
        if progress_bar:
            bar = Bar("Processing: ", max=self.end_time)

        for i in range(self.end_time):
            vehicles = traci.vehicle.getIDList()
            # arrived = traci.simulation.getArrivedIDList()
            # departed_vehicles = traci.simulation.getDepartedIDList()
            # print(traci.simulation.getCurrentTime(), len(vehicles), len(departed_vehicles), len(arrived), departed_vehicles, arrived)
            # for veh in vehicles:
            #     xy = traci.vehicle.getPosition(veh)
            # print(xy)
            # if len(vehicles) > 0:
            #     r = traci.vehicle.getRoute(vehicles[0])
            #     rs = traci.rerouter.
            #     print(rs)
            # self.step_sim()
            # print(i)
            self.simulation_step()

            if progress_bar:
                bar.next()

        if progress_bar:
            bar.finish()

    # def step_sim(self):
    #     # The monaco scenario expects .25s steps instead of 1s, account for that here.
    #     for _ in range(1):
    #         self.sumo.simulationStep()
    def simulation_step(self):
        traci.simulationStep()
