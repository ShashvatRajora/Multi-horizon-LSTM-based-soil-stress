# “We simulate real-time IoT data streaming using historical sensor datasets. 
import pandas as pd
import time

class IoTSimulator:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.index = 0

    def stream(self):
        if self.index < len(self.data):
            row = self.data.iloc[self.index]
            self.index += 1
            return row.to_dict()
        return None

def run_simulation(simulator, delay=1):
    while True:
        data = simulator.stream()
        if data is None:
            break
        
        print("Streaming Data:", data)
        time.sleep(delay)