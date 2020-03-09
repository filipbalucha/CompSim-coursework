from TrafficSimulation import TrafficSimulation


class TrafficSimulationTest(object):
    # Calculate steady state velocity for a given car density
    def calculate(self):
        density = 0.8
        road_length = 100
        ts = TrafficSimulation(road_length)
        print(
            f"Steady state average speed for {density*100}% density is: {ts.ss_avg_speed(density)}")

    # Plot steady state velocity against car density
    def plot(self):
        road_length = 1000
        density_from = 0.01
        density_to = 1
        num_samples = 400
        ts = TrafficSimulation(road_length)
        ts.plot(density_from, density_to, num_samples)

    # Animate consequent traffic steps
    def animation(self):
        road_length = 25
        density = 0.6
        num_iterations = 200
        ts = TrafficSimulation(road_length)
        ts.animation(density, num_iterations)


if __name__ == "__main__":
    tst = TrafficSimulationTest()
    tst.calculate()
    tst.plot()
    # tst.animation()
