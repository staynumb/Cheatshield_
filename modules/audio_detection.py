import numpy as np
import sounddevice as sd
import tensorflow as tf
import tensorflow_hub as hub
import threading
import csv
import io
import urllib.request

class AudioDetector:
    def __init__(self, sample_rate=16000, chunk_size=1024, detection_interval=5.0):
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.detection_interval = detection_interval
        self.model = hub.load('https://tfhub.dev/google/yamnet/1')
        
        # Load YAMNet class map to get correct indices
        class_map_url = 'https://raw.githubusercontent.com/tensorflow/models/master/research/audioset/yamnet/yamnet_class_map.csv'
        try:
            response = urllib.request.urlopen(class_map_url)
            class_map_csv = response.read().decode('utf-8')
            reader = csv.reader(io.StringIO(class_map_csv))
            next(reader)  # skip header
            self.yamnet_classes = [row[2] for row in reader]
        except Exception:
            # Fallback: YAMNet Speech=0, Whispering is not at index 1
            # Use known indices from YAMNet class map
            self.yamnet_classes = None
        
        # Find correct indices for target classes
        self.target_classes = {'Speech': None, 'Whispering': None}
        if self.yamnet_classes:
            for i, name in enumerate(self.yamnet_classes):
                if name == 'Speech':
                    self.target_classes['Speech'] = i
                elif name == 'Whispering':
                    self.target_classes['Whispering'] = i
        
        # Fallback to known YAMNet indices if lookup failed
        if self.target_classes['Speech'] is None:
            self.target_classes['Speech'] = 0  # Speech is actually at index 0
        if self.target_classes['Whispering'] is None:
            self.target_classes['Whispering'] = 14  # Whispering known index
        
        self.audio_buffer = []
        self.running = True
        self.lock = threading.Lock()

    def detect_audio(self):
        try:
            # Record audio
            audio = sd.rec(int(self.detection_interval * self.sample_rate), samplerate=self.sample_rate, channels=1, blocking=True)
            audio = audio.flatten()
            
            # Debug: Print audio data statistics
            print(f"Audio data - Mean: {np.mean(audio):.4f}, Max: {np.max(audio):.4f}, Min: {np.min(audio):.4f}")
            
            # Normalize audio to [-1, 1]
            max_val = np.max(np.abs(audio))
            if max_val > 1e-7:
                audio = audio / max_val
            else:
                return False, 0.0, ""  # Silent audio, skip
            
            # Ensure audio is float32 for TF
            audio = audio.astype(np.float32)
            
            # Ensure audio is at 16kHz
            if len(audio) < self.sample_rate:
                audio = np.pad(audio, (0, self.sample_rate - len(audio)), 'constant')
            audio = audio[:self.sample_rate]
            
            # Run YAMNet model
            scores, _, _ = self.model(audio)
            scores = scores.numpy()
            
            # Average scores over time
            avg_scores = np.mean(scores, axis=0)
            
            # Check for suspicious sounds using correct indices
            speech_idx = self.target_classes['Speech']
            whisper_idx = self.target_classes['Whispering']
            
            speech_confidence = avg_scores[speech_idx]
            whisper_confidence = avg_scores[whisper_idx]
            
            # Lowered threshold for speech detection
            if speech_confidence > 0.3 or whisper_confidence > 0.3:
                if speech_confidence > whisper_confidence:
                    return True, speech_confidence, f"Suspicious sound detected - Speech (Confidence: {speech_confidence:.2f})"
                else:
                    return True, whisper_confidence, f"Suspicious sound detected - Whispering (Confidence: {whisper_confidence:.2f})"
            
            return False, 0.0, ""
        
        except Exception as e:
            print(f"Error in audio detection: {e}")
            return False, 0.0, ""

    def close(self):
        self.running = False