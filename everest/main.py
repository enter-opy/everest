import numpy as np
import tensorflow as tf
import os

model_path = os.path.join(os.path.dirname(__file__), 'model.h5')
model = tf.keras.models.load_model(model_path)

window_size = 20
hop_size = 5

def find_peaks(X, threshold=0.5, return_probs=True):
    """
    Parameters:
    - X (array-like): Input array representing the signal.
    - threshold (float): Probability threshold for identifying peaks.

    Returns:
    - peaks_loc (ndarray): Locations of the peaks.
    - peaks_mag (ndarray): Values of the peaks.
    - probs (ndarray): Probabilities associated with each peak.
    """

    assert isinstance(X, (np.ndarray)), "Input must be of type numpy.array."
    assert 0 <= threshold <= 1, "Threshold must be between 0 and 1."

    peaks_loc = []
    probs = []
    l = 0

    while l < len(X) - window_size:
        X_window = np.array([X[l: l + window_size]])
        X_window = X_window[..., np.newaxis]

        prediction = model.predict(X_window, verbose=False)[0, 0]

        if prediction > threshold:
            peak_loc = l + np.argmax(X[l: l + window_size])

            if peak_loc not in peaks_loc:
                peaks_loc.append(peak_loc)
                if return_probs:
                    probs.append(prediction)
        
        l += hop_size

    peaks_val = X[peaks_loc]

    peaks_loc = np.array(peaks_loc)
    peaks_val = np.array(peaks_val)

    if return_probs:
        probs = np.array(probs)
        return peaks_loc, peaks_val, probs
    else:
        return peaks_loc, peaks_val




