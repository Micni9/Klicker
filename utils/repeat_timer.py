from threading import Timer

class RepeatTimer(Timer):
    def run(self):
        self.finished.wait(self.interval)
        while not self.finished.is_set():
            self.function(*self.args,**self.kwargs)
            self.finished.wait(self.interval)