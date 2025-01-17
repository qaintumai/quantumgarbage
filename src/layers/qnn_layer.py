# Copyright 2024 The qAIntum.ai Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import pennylane as qml

class QuantumNeuralNetworkLayer:
    """
    A class used to define a Quantum Neural Network Layer for photonic quantum computing.

    Usage:
    To use the QuantumNeuralNetworkLayer class, import it as follows:
    from layers.quantum_layer import QuantumNeuralNetworkLayer

    Example:
    qnn_layer = QuantumNeuralNetworkLayer(num_wires=4)
    qnn_layer.apply(params)
    """

    def __init__(self, num_wires):
        """
        Initializes the QuantumNeuralNetworkLayer class with the given number of wires.

        Parameters:
        - num_wires (int): Number of wires (qumodes) in the quantum circuit.
        """
        self.num_wires = num_wires

    def apply(self, v):
        """
        Applies the quantum neural network layer with the given parameters.

        Parameters:
        - v (list or array): List or array of parameters for the quantum gates.

        Returns:
        - None
        """
        num_params = len(v)

        # Interferometer 1
        for i in range(self.num_wires - 1):
            idx = i * 2
            if idx + 1 < num_params:
                theta = v[idx]
                phi = v[idx + 1]
                qml.Beamsplitter(theta, phi, wires=[i % self.num_wires, (i + 1) % self.num_wires])

        for i in range(self.num_wires):
            idx = (self.num_wires - 1) * 2 + i
            if idx < num_params:
                qml.Rotation(v[idx], wires=i)

        # Squeezers
        for i in range(self.num_wires):
            idx = (self.num_wires - 1) * 2 + self.num_wires + i
            if idx < num_params:
                qml.Squeezing(v[idx], 0.0, wires=i)

        # Interferometer 2
        for i in range(self.num_wires - 1):
            idx = (self.num_wires - 1) * 2 + self.num_wires + self.num_wires + i * 2
            if idx + 1 < num_params:
                theta = v[idx]
                phi = v[idx + 1]
                qml.Beamsplitter(theta, phi, wires=[i % self.num_wires, (i + 1) % self.num_wires])

        for i in range(self.num_wires):
            idx = (self.num_wires - 1) * 2 + self.num_wires + self.num_wires + (self.num_wires - 1) * 2 + i
            if idx < num_params:
                qml.Rotation(v[idx], wires=i)

        # Bias addition
        for i in range(self.num_wires):
            idx = (self.num_wires - 1) * 2 + self.num_wires + self.num_wires + (self.num_wires - 1) * 2 + self.num_wires + i
            if idx < num_params:
                qml.Displacement(v[idx], 0.0, wires=i)

        # Non-linear activation function
        for i in range(self.num_wires):
            idx = (self.num_wires - 1) * 2 + self.num_wires + self.num_wires + (self.num_wires - 1) * 2 + self.num_wires + self.num_wires + i
            if idx < num_params:
                qml.Kerr(v[idx], wires=i)
