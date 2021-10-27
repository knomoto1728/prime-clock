import collections
import datetime
import threading
import time
import tkinter as tk


class PrimeClock(object):

    def __init__(self):
        self.root = tk.Tk()
        self.root.title(u'Prime Clock')
        self.label = tk.Label(self.root)
        self.label['font'] = ('System', 50)
        self.label["bg"] = "deep sky blue"
        self.label["fg"] = "white"
        self.label.grid(column=0, row=0)
    
    def changeLabelText(self):
        while True:
            time_number = datetime.datetime.now().strftime('%m%d%H%M')
            self.label['text'] = self.primes_to_letters(self.prime_factorization(int(time_number)))
            time.sleep(60)

    def prime_factorization(self, n):
        primes = []
        while n % 2 == 0:
            primes.append(2)
            n //= 2
        prime = 3
        while prime * prime <= n:
            if n % prime == 0:
                primes.append(prime)
                n //= prime
            else:
                prime += 2
        if n != 1:
            primes.append(n)
        return collections.Counter(primes)
    
    def primes_to_letters(self, dict):
        letters = []
        for prime, index in dict.items():
            text = str(prime) + '^' + str(index)
            letters.append(text)
        return ' * '.join(letters)

if __name__ == '__main__':
    timer = PrimeClock()
    thread = threading.Thread(target=timer.changeLabelText, daemon=True)
    thread.start()
    timer.root.mainloop()