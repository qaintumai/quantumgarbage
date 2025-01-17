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

import unittest
import pennylane as qml
import torch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from layers.qnn_layer import QuantumNeuralNetworkLayer

class TestQuantumNeuralNetworkLayer(unittest.TestCase):

    def setUp(self):
        """
        Initialize a quantum device and a QuantumNeuralNetworkLayer instance for testing.
        """
        self.num_wires = 4  # Example number of wires
        self.qnn_layer = QuantumNeuralNetworkLayer(num_wires=self.num_wires)

        # # Use PennyLane's default.qubit simulator for testing
        # self.dev = qml.device("default.qubit", wires=self.num_wires)

        self.dev = qml.device("strawberryfields.fock", wires=self.num_wires, cutoff_dim=2)

    def test_layer_applies_correct_operations(self):
        """
        Test that the QuantumNeuralNetworkLayer applies the correct operations based on the parameters.
        """
        params = torch.tensor([0.1] * (self.num_wires * 5))  # Example parameters

        # Quantum circuit to apply the layer
        @qml.qnode(self.dev)
        def circuit(params):
            self.qnn_layer.apply(params)
            # return [qml.expval(qml.PauliZ(i)) for i in range(self.num_wires)]
            return [qml.expval(qml.X(wire)) for wire in range(self.num_wires)]

        output = circuit(params)

        # Assert that the circuit ran successfully and returns an output of expected size
        self.assertEqual(len(output), self.num_wires)

    def test_circuit_with_varied_params(self):
        """
        Test that the QuantumNeuralNetworkLayer can handle varying parameter lengths.
        """
        params_short = torch.tensor([0.1] * (self.num_wires * 3))  # Shorter list of parameters
        params_long = torch.tensor([0.1] * (self.num_wires * 7))   # Longer list of parameters

        @qml.qnode(self.dev)
        def circuit(params):
            self.qnn_layer.apply(params)
            # return [qml.expval(qml.PauliZ(i)) for i in range(self.num_wires)]
            return [qml.expval(qml.X(wire)) for wire in range(self.num_wires)]

        output_short = circuit(params_short)
        output_long = circuit(params_long)

        # Ensure both circuits run successfully with different parameter lengths
        self.assertEqual(len(output_short), self.num_wires)
        self.assertEqual(len(output_long), self.num_wires)

    def test_apply_invalid_params(self):
        """
        Test that an error is raised when invalid parameters are passed to the apply function.
        """
        # Create a set of parameters that do not fit the expected structure
        invalid_params = torch.tensor([0.1] * (self.num_wires * 2))  # Not enough parameters

        @qml.qnode(self.dev)
        def circuit(params):
            self.qnn_layer.apply(params)
            # return [qml.expval(qml.PauliZ(i)) for i in range(self.num_wires)]
            # wires = list(range(self.num_wires))
            # return [qml.probs(wires=wires)]
            return [qml.expval(qml.X(wire)) for wire in range(self.num_wires)]

        # Expecting an exception due to invalid parameter length
        with self.assertRaises(IndexError):
            circuit(invalid_params)

    def test_apply_edge_case_params(self):
        """
        Test the application of edge-case parameters, such as zeros or extreme values.
        """
        zero_params = torch.zeros(self.num_wires * 5)
        extreme_params = torch.tensor([100.0] * (self.num_wires * 5))  # Extreme parameter values

        @qml.qnode(self.dev)
        def circuit(params):
            self.qnn_layer.apply(params)
            # return [qml.expval(qml.PauliZ(i)) for i in range(self.num_wires)]
            # wires = list(range(self.num_wires))
            # return [qml.probs(wires=wires)]
            return [qml.expval(qml.X(wire)) for wire in range(self.num_wires)]

        output_zero = circuit(zero_params)
        output_extreme = circuit(extreme_params)

        # Ensure the circuit runs without errors
        self.assertEqual(len(output_zero), self.num_wires)
        self.assertEqual(len(output_extreme), self.num_wires)

if __name__ == '__main__':
    unittest.main()
