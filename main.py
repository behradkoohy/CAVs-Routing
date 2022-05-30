import argparse
import configparser
import os
from simulation import Simulation


def main():
    ap = argparse.ArgumentParser()
    # ap.add_argument()
    ap.add_argument(
        "--sumoconf",
        type=str,
        default=None,
        help="sumocfg file for simulation. If provided net and route are ignored.",
    )
    ap.add_argument(
        "--net",
        type=str,
        default=None,
        help="net.xml file for simulation. Ignored if sumocfg provided.",
    )
    ap.add_argument(
        "--route",
        type=str,
        default=None,
        help="rou.xml file for simulation. Ignored if sumocfg provided.",
    )
    args = ap.parse_args()

    cfg = configparser.ConfigParser()
    cfg.read("immutable.init")

    sumocfg = cfg.get("INPUT", "sumocfg", fallback=args.sumoconf)
    net = cfg.get("INPUT", "net", fallback=args.net)
    route = cfg.get("INPUT", "route", fallback=args.route)
    log_dir = cfg.get("OUTPUT", "log_dir", fallback="logs/")
    print("Output Directory", log_dir)

    sim = Simulation(
        run_name="test",
        map_name=map,
        net=net,
        conf=sumocfg,
        route=route,
        log_dir=log_dir,
    )


if __name__ == "__main__":
    main()
