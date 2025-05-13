import numpy as np

class NeuralNetwork:
    def __init__(self, layers, activation_functions, loss_function='mse'):
        self.layers = layers
        self.activation_functions = activation_functions
        self.loss_function = loss_function
        
        # Initialize weights, biases, and their gradients
        self.weights = []
        self.biases = []
        self.weights_gradients = []
        self.biases_gradients = []
        self.layer_outputs = []
        self.layer_activations = []
        
        self.initialize_weights_and_biases()

    def initialize_weights_and_biases(self):
        np.random.seed(42)
        
        for i in range(1, len(self.layers)):
            # Xavier initialization for weights
            in_units = self.layers[i - 1]
            out_units = self.layers[i]
            limit = np.sqrt(6.0 / (in_units + out_units))
            W = np.random.uniform(-limit, limit, (out_units, in_units))
            b = np.zeros((out_units, 1))
            
            self.weights.append(W)
            self.biases.append(b)
            self.weights_gradients.append(np.zeros_like(W))
            self.biases_gradients.append(np.zeros_like(b))
        
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def sigmoid_prime(self, z):
        sig = self.sigmoid(z)
        return sig * (1 - sig)
    
    def tanh(self, z):
        return np.tanh(z)

    def tanh_prime(self, z):
        return 1 - np.tanh(z) ** 2
    
    def relu(self, z):
        return np.maximum(0, z)

    def relu_prime(self, z):
        return (z > 0).astype(float)
    
    def leaky_relu(self, z):
        return np.where(z > 0, z, z * 0.01)
    
    def leaky_relu_prime(self, z):
        return np.where(z > 0, 1.0, 0.01)
    
    def linear(self, z):
        return z

    def linear_prime(self, z):
        return np.ones_like(z)
    
    def get_activation_function(self, layer_idx):
        activation_name = self.activation_functions[layer_idx]
        if activation_name == 'sigmoid':
            return self.sigmoid, self.sigmoid_prime
        elif activation_name == 'tanh':
            return self.tanh, self.tanh_prime
        elif activation_name == 'relu':
            return self.relu, self.relu_prime
        elif activation_name == 'leaky_relu':
            return self.leaky_relu, self.leaky_relu_prime
        elif activation_name == 'linear':
            return self.linear, self.linear_prime
        else:
            raise ValueError(f"Activation function '{activation_name}' not recognized")

    def mse_loss(self, y, y_hat):
        return 0.5 * np.mean(np.square(y - y_hat))
    
    def mse_loss_prime(self, y, y_hat):
        return y_hat - y
    
    def binary_cross_entropy_loss(self, y, y_hat):
        y_hat = np.clip(y_hat, 1e-7, 1 - 1e-7)
        return -np.mean(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))
    
    def binary_cross_entropy_loss_prime(self, y, y_hat):
        y_hat = np.clip(y_hat, 1e-7, 1 - 1e-7)
        return (y_hat - y) / (y_hat * (1 - y_hat))
    
    def get_loss_function(self):
        if self.loss_function == 'mse':
            return self.mse_loss, self.mse_loss_prime
        elif self.loss_function == 'binary_cross_entropy':
            return self.binary_cross_entropy_loss, self.binary_cross_entropy_loss_prime
        else:
            raise ValueError(f"Loss function '{self.loss_function}' not recognized")
    
    def feedforward(self, X):
        self.layer_outputs = []
        self.layer_activations = []
        
        A = X
        self.layer_activations.append(A)
        
        for i in range(len(self.layers) - 1):
            Z = np.dot(self.weights[i], A) + self.biases[i]
            A_func, _ = self.get_activation_function(i)
            A = A_func(Z)
            self.layer_outputs.append(Z)
            self.layer_activations.append(A)
        
        return self.layer_activations[-1]

    def backpropagate(self, X, y):
        m = X.shape[1]
        loss_func, loss_func_prime = self.get_loss_function()
        
        # Calculate the loss derivative with respect to the output
        A = self.feedforward(X)
        loss_derivative = loss_func_prime(y, A)
        
        # Backpropagate through the network
        for i in reversed(range(len(self.layers) - 1)):
            A_prev = self.layer_activations[i]
            Z = self.layer_outputs[i]
            A_func, A_func_prime = self.get_activation_function(i)
            dA = loss_derivative * A_func_prime(Z)
            
            dW = np.dot(dA, A_prev.T) / m
            db = np.sum(dA, axis=1, keepdims=True) / m
            
            # Store gradients
            self.weights_gradients[i] = dW
            self.biases_gradients[i] = db
            
            # Update loss_derivative for the next layer
            loss_derivative = np.dot(self.weights[i].T, dA)

    def update_parameters(self, learning_rate=0.01):
        for i in range(len(self.layers) - 1):
            self.weights[i] -= learning_rate * self.weights_gradients[i]
            self.biases[i] -= learning_rate * self.biases_gradients[i]

    def train(self, X, y, epochs=100, batch_size=32, learning_rate=0.01):
        for epoch in range(epochs):
            # Shuffle data
            indices = np.random.permutation(X.shape[1])
            X_shuffled = X[:, indices]
            y_shuffled = y[:, indices]
            
            for i in range(0, X.shape[1], batch_size):
                # Mini-batch
                X_batch = X_shuffled[:, i:i+batch_size]
                y_batch = y_shuffled[:, i:i+batch_size]
                
                # Backpropagation and parameter update
                self.backpropagate(X_batch, y_batch)
                self.update_parameters(learning_rate)
            
            if epoch % 10 == 0:
                # Print loss every 10 epochs
                A = self.feedforward(X)
                loss = self.mse_loss(y, A) if self.loss_function == 'mse' else self.binary_cross_entropy_loss(y, A)
                print(f"Epoch {epoch}/{epochs}, Loss: {loss}")

# Example usage:

# Define the network structure (input layer, two hidden layers, output layer)
layers = [2, 3, 3, 1]
activation_functions = ['relu', 'relu', 'sigmoid']

# Initialize the neural network
nn = NeuralNetwork(layers, activation_functions, loss_function='mse')

# Example input and output for training
X = np.array([[0, 0, 1, 1], [0, 1, 0, 1],[1,0,1,0],[1,1,0,0]])  # 4 samples, 4 features
y = np.array([[0, 1, 1, 0]])  # XOR output

# Train the network
nn.train(X, y, epochs=1000, batch_size=4, learning_rate=0.1)

