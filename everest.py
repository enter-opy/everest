import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('model/model.h5')

window_size = 20
hop_size = 5

def find_peaks(X, threshold=0.5):
    """
    Parameters:
    - X (array-like): Input array representing the signal.
    - threshold (float): Probability threshold for identifying peaks.

    Returns:
    - peaks_loc (ndarray): Locations of the peaks.
    - peaks_mag (ndarray): Values of the peaks.
    - probs (ndarray): Probabilities associated with each peak.
    """

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
                probs.append(prediction)
        
        l += hop_size

    peaks_val = X[peaks_loc]

    peaks_loc = np.array(peaks_loc)
    peaks_val = np.array(peaks_val)
    probs = np.array(probs)

    return peaks_loc, peaks_val, probs




