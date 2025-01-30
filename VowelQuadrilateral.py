# A short description of this code

# This is a code to plot overalapping vowel quadrilaterals

# Instructions, Read Carefully!

# You will need the values of first and second formants (F1, & F2)
# You can obtain those from recordings of the four words below
# Word list: Heat, Hat, Hot, and Hoot
# Use any software that does acoustic analysis, such as Praat
# https://www.fon.hum.uva.nl/praat/
# to measure the formant frequencies

# Enter the formant values in the data block below for 'Normal"
# Only change values in lines 27, 29, 31, and 33
# Do not change the values from Watrous 1991, which are provided

# The plot generated can be edited and saved in various formats
# Please be sure to cite the three sources below if you use this code

# Reference 1:
# Peterson, G., & Barney, H. (1952).
# Control methods used in a study of the vowels.
# The Journal of Acoustical Society of America, 24(2), 175-184.
# https://doi.org/10.1121/1.1906875

# Reference 2: 
# Watrous, R. (1991).
# Current status of Peterson-Barney vowel formant data.
# The Journal of Acoustical Society of America, 89(5), 2459-2460.
# https://doi.org/10.1121/1.400932

# Reference 3:
# Rami, M. K. (2025).
# Vowel Quadrilaterals
#


import matplotlib.pyplot as plt

import numpy as np

from scipy.spatial.distance import cdist

# Sample data -normal data entered below for two speakers
data = [
    {'vowel': 'Heat', 'speaker': 'Normal', 'F1': 267, 'F2': 2294},
    {'vowel': 'Heat', 'speaker': 'Watrous 1991', 'F1': 267, 'F2': 2294},
    {'vowel': 'Hat', 'speaker': 'Normal', 'F1': 664, 'F2': 1727},
    {'vowel': 'Hat', 'speaker': 'Watrous 1991', 'F1': 664, 'F2': 1727},
    {'vowel': 'Hot', 'speaker': 'Normal', 'F1': 718, 'F2': 1091},
    {'vowel': 'Hot', 'speaker': 'Watrous 1991', 'F1': 718, 'F2': 1091},
    {'vowel': 'Hoot', 'speaker': 'Normal', 'F1': 437, 'F2': 1023},
    {'vowel': 'Hoot', 'speaker': 'Watrous 1991', 'F1': 437, 'F2': 1023},
]

# Extract unique speakers and vowels
speakers = list(set(d['speaker'] for d in data))
vowels = list(set(d['vowel'] for d in data))

# Define colors and markers for each speaker
colors = {'Normal': 'red', 'Watrous 1991': 'blue'}
markers = {'Normal': 'o', 'Watrous 1991': 's'}
plt.figure(figsize=(10, 8))
for speaker in speakers:

    # Filter data for the current speaker
    speaker_data = [d for d in data if d['speaker'] == speaker]
    F1 = [d['F1'] for d in speaker_data]
    F2 = [d['F2'] for d in speaker_data]
    vowel_labels = [d['vowel'] for d in speaker_data]
 
 # Plot the vowel points
    plt.scatter(F2, F1, label=speaker, edgecolor='black', linewidth=0.5, alpha=0.7)
 
 # Annotate each point with the vowel label
    for f2, f1, vowel in zip(F2, F1, vowel_labels):
        plt.text(f2, f1, vowel, fontsize=14, ha='right')
 
   # Find nearest-neighbor order
    points = np.array(list(zip(F2, F1)))
    dist_matrix = cdist(points, points)
    np.fill_diagonal(dist_matrix, np.inf)  # Avoid self-loops
    path = [0]  # Start from the first point
    while len(path) < len(points):
        last_point = path[-1]
        next_point = np.argmin(dist_matrix[last_point])
        path.append(next_point)
        dist_matrix[:, last_point] = np.inf  # Mark as visited

    # Reorder points based on nearest-neighbor path
    F1_ordered = points[path, 1]
    F2_ordered = points[path, 0]
    plt.plot(F2_ordered, F1_ordered, c=colors[speaker], alpha=0.5)

    # Add the first point to the end to close the loop
    F1_ordered = np.append(F1_ordered, F1_ordered[0])
    F2_ordered = np.append(F2_ordered, F2_ordered[0])

    plt.plot(F2_ordered, F1_ordered, c=colors[speaker], alpha=0.5)

plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.xlabel('Second Formant Frequency (Hz)')
plt.ylabel('First Formant Frequency (Hz)')

# Use the lines below if you want to add a title, a legent, and a grid
# Only edit the text within parentheses for title and legent
# Remove the hashmarks in front of the lines to activate them

# plt.title('Overlapping Vowel Quadrilaterals for speaker as compared to vowel norms')
# plt.legend(title='Speech',loc='lower left', fontsize=12, title_fontsize=14)
# plt.grid(True)
plt.show()
