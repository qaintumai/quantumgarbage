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

# Test the DecoderBlock class
import torch
import sys
import os

# Add the src directory to the Python path
script_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(script_dir, '..', 'src'))
if src_dir not in sys.path:
    sys.path.append(src_dir)

from models import QuantumDecoder
from layers import qnn_circuit

def test_decoder_block():
    # Define parameters
    embed_len = 64
    num_heads = 8
    num_layers = 2
    num_wires = 6
    quantum_nn = qnn_circuit
    seq_len = 10
    batch_size = 32
    dropout = 0.1
    mask = None

    # Create an instance of DecoderBlock
    model = QuantumDecoder(embed_len, num_heads, num_layers, num_wires, quantum_nn, batch_size, dropout, mask)

    # Create dummy input tensors
    target = torch.rand(batch_size, seq_len, embed_len)
    encoder_output = torch.rand(batch_size, seq_len, embed_len)

    # Forward pass
    output = model(target, encoder_output)

    # Check the output shape
    assert output.shape == (
        batch_size, seq_len, embed_len), f"Expected output shape {(batch_size, seq_len, embed_len)}, but got {output.shape}"

    # Check the output type
    assert isinstance(
        output, torch.Tensor), f"Expected output type torch.Tensor, but got {type(output)}"

    print("Test passed!")

    return output.shape

test_decoder_block()