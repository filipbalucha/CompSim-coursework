from TrafficSimulation import TrafficSimulation


class TrafficSimulationTest(object):
    def plot(self):
        road_length = 1000
        density_from = 0.01
        density_to = 1
        num_samples = 400
        ts = TrafficSimulation(road_length)
        ts.plot(density_from, density_to, num_samples)

    def calculate(self):
        density = 0.8
        road_length = 10
        ts = TrafficSimulation(road_length)
        print(
            f"Steady state average speed for {density*100}% density is: {ts.ss_avg_speed(density)}")

    def animation(self):
        road_length = 100
        density = 0.6
        num_iterations = 200
        tsa = TrafficSimulation(road_length)
        tsa.animate(density, num_iterations)


if __name__ == "__main__":
    tst = TrafficSimulationTest()
    # tst.plot()
    # tst.calculate()
    tst.animation()
