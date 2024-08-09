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

# Train qnn_model parameters

import torch

def train_model(model, criterion, optimizer, train_loader, num_epochs=100, device='cpu', debug=True):
    """
    Trains the given model.

    Parameters:
    - model: torch.nn.Module, the model to train
    - criterion: loss function
    - optimizer: optimizer for updating model parameters
    - train_loader: DataLoader, provides an iterable over the dataset
    - num_epochs: int, number of epochs to train the model (default: 100)
    - device: str, device to use for training ('cpu' or 'cuda')
    - debug: bool, if True, print debug information

    Returns:
    - None
    """
    model.to(device)  # Move model to the specified device

    for epoch in range(num_epochs):
        model.train()  # Set the model to training mode
        running_loss = 0.0
        operation_count = 0

        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device).float(), labels.to(device).float()
            if debug:
                print(f"Epoch {epoch + 1}, Batch {operation_count + 1}")
                print(f"Inputs: {inputs.shape}, Labels: {labels.shape}")

            # Forward pass
            outputs = model(inputs)
            if debug:
                print(f"Outputs: {outputs.shape}")
            loss = criterion(outputs, labels)
            if debug:
                print(f"Loss: {loss.item()}")

            # Backward pass and optimization
            optimizer.zero_grad()  # Zero the gradients
            loss.backward()  # Backpropagation
            optimizer.step()  # Update model parameters
            if debug:
                print("Performed backpropagation and optimization step")

            running_loss += loss.item() * inputs.size(0)
            operation_count += 1

        epoch_loss = running_loss / len(train_loader.dataset)
        if (epoch + 1) % 10 == 0 or debug:
            print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {epoch_loss:.4f}')
        if debug:
            print(f"Total operations in epoch {epoch + 1}: {operation_count}")

    print("Training complete")

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the given model.

    Parameters:
    - model: torch.nn.Module, the model to evaluate
    - X_test: torch.Tensor, the test data
    - y_test: torch.Tensor, the test labels

    Returns:
    - None
    """
    model.eval()  # Set the model to evaluation mode
    with torch.no_grad():
        # Forward pass
        y_pred = model(X_test)
        
        # Convert logits or probabilities to class predictions (e.g., using argmax)
        y_pred = torch.argmax(y_pred, dim=1)
        
        # Ensure both y_pred and y_test are on the same device and in the same format
        y_pred = y_pred.cpu().numpy()
        y_test = y_test.cpu().numpy()

        # Calculate accuracy
        correct = (y_pred == y_test).sum()
        accuracy = correct / len(y_test)
        print(f"Accuracy: {accuracy * 100:.2f}%")
