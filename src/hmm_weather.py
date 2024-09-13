import numpy as np
from hmmlearn import hmm

# Define the state space
states = ['Hot', 'Cold']
n_states = len(states)
print("Number of states: " + str(n_states))

# Define the observation space
observations = ['1', '2', '3']
n_observations = len(observations)
print("Number of observations: " + str(n_observations))

# Define the initial state probabilities
start_probability = np.array([0.8, 0.2])
print("Initial state probabilities: " + str(start_probability))

# Define the state transition probabilities
transition_probability = np.array([[0.7, 0.3],
                                    [0.4, 0.6]])
print("State transition probabilities: " + str(transition_probability))

# Define the observation likelihoods
emission_probability = np.array([[0.2, 0.4, 0.4],
                                 [0.5, 0.4, 0.1]])
print("Observation likelihoods: " + str(emission_probability))

# Create the model
model = hmm.CategoricalHMM(n_components=n_states)
model.startprob_ = start_probability
model.transmat_ = transition_probability
model.emissionprob_ = emission_probability

# Define the sequence of observations
observations_sequence_1 = np.array([3, 1, 2, 3, 1, 2, 3, 1, 2]) - 1
observations_sequence_1 = observations_sequence_1.reshape(-1, 1)
observations_sequence_2 = np.array([3, 1, 1, 2, 3, 3, 1, 1, 2]) - 1 
observations_sequence_2 = observations_sequence_2.reshape(-1, 1)

# Predict the most likely sequence of hidden states
hidden_states_1 = model.predict(observations_sequence_1, len(observations_sequence_1))
hidden_states_2 = model.predict(observations_sequence_2, len(observations_sequence_2))

# Print the most likely sequence of hidden states
log_prob_1, hidden_states_1 = model.decode(observations_sequence_1,
                                           lengths = len(observations_sequence_1),
                                           algorithm="viterbi")

log_prob_2, hidden_states_2 = model.decode(observations_sequence_2,
                                           lengths = len(observations_sequence_2),
                                           algorithm="viterbi")

print("Most likely sequence of hidden states for sequence 1: " + str(hidden_states_1))
print("Most likely sequence of hidden states for sequence 2: " + str(hidden_states_2))