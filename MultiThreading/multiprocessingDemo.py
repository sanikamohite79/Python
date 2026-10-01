from multiprocessing import Process

def calculate():
    total = 0

    for i in range(10_000_000):
        total += i
    print(total)

#On Windows, when a new process starts, 
#Python starts a fresh Python interpreter and imports your main file again.
#"Only the original/main program should create the processes."
if __name__ == "__main__":

   p1 = Process(target = calculate)
   p2 = Process(target = calculate)

   p1.start()
   p2.start()

   p1.join()
   p2.join()

   print("completed")