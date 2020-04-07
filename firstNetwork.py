from pyltes.network import CellularNetwork

network = CellularNetwork()
network.Generator.createHexagonalBSdeployment(1666)

network.Generator.insertUErandomly(100)
network.connectUsersToTheBestBS()

network.Printer.drawHistogramOfUEThroughput("thrHistogram")
network.Printer.drawNetwork(fillMethod="SINR", filename="sinrMap")
network.Printer.drawNetwork(fillMethod="Sectors", filename="secorsMap")
