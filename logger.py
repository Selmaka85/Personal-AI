# logger.py

class Logger:
    def save_logs(self, input_data, output, score):
        print("LOG:", {"input": input_data, "output": output, "score": score})

    def monitor_usage(self):
        pass

    def flag_anomalies(self):
        pass