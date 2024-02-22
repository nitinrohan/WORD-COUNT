import os
import threading

def create_p_file():
    if not os.path.exists("CHAPTER"):
        os.makedirs("CHAPTER")

    with open("data.txt", "r") as f:
        index = 1
        for p in f.read().split("\n\n"):
            f_n = f"p_{index}.txt"
            index += 1
            path = "CHAPTER" + "/" + f_n
            with open(path, "w") as fn:
                fn.write(p)

def c_w(fn, w_c):
    path = "CHAPTER" + "/" + fn
    with open(path, 'r') as f:
        words = f.read().lower().split()
        for w in words:
            w = w.strip("'!,.")
            if w in w_c:
                w_c[w] += 1
            else:
                w_c[w] = 1

def process(f_n, w_c):
    for fn in f_n:
        c_w(fn, w_c)            

def wc_multiThread(fns):
    w_c = {}
    t = []
    for i in range(no_thread):
        thread = threading.Thread(target= process, args=(fns[i::no_thread], w_c))
        t.append(thread)
        thread.start()

    for thread in t:
        thread.join()
    
    return w_c

if __name__ == '__main__':
    no_thread = 15
    create_p_file()

    files = [fn for fn in os.listdir("CHAPTER") if fn.endswith('.txt')]

    w_c  = wc_multiThread(files)

    with open('w_c.txt', 'w') as c_f:
        for w, c in w_c.items():
            c_f.write(f"{w}: {c}\n")
    
    print("Word Count File Created Successfully!")