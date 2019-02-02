#pragma once
#include <vector>
#include <cstdlib>
#include "net.h"

struct Connection
{
	double weight;
	double deltaWeight;
};

class Neuron
{
public:
	Neuron(int numOutputs, int myIndex);
	//~Neuron();
	void feedForward(const Layer &prevLayer);
	void setOutputVal(double val) { m_outputVal = val; }
	double getOutputVal() const { return m_outputVal; }
	void calcOutputGradients(double targetVal);
	void calcHiddenGradients(const Layer &nextLayer);





private:
	static double randomWeight() { return rand() / double(RAND_MAX); }
	double m_outputVal;
	std::vector<Connection> m_outputWeights;
	double m_myIndex;
	double m_gradient;
	static double transferFunction(double x);
	static double transferFunctionDerivative(double x);

};

