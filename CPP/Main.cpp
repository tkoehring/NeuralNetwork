#include <vector>
#include "net.h"

int main()
{
	std::vector<unsigned> topology;
	topology.push_back(3);
	topology.push_back(2);
	topology.push_back(1);
	Net nNet(topology);

	std::vector<double> inputVals;
	//nNet.feedForward(inputVals);

	std::vector<double> targetVals;
	//nNet.backProp(targetVals);

	std::vector<double> resultVals;
	//nNet.getResults(resultVals);


}

