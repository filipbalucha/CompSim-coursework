from TrafficSimulation import TrafficSimulation


class TrafficSimulationTest(object):
    def run(self):
        traffic_simulation = TrafficSimulation()
        traffic_simulation.steady_state_avg_speed(0.6, 10)


if __name__ == "__main__":
    traffic_simulation_test = TrafficSimulationTest()
    traffic_simulation_test.run()
