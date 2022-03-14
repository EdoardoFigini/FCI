import requests
from matplotlib import pyplot as plt


def main():
    url = 'http://www.google.com'
    #print(r.text)
    #print(f'Ritardo: {r.elapsed.microseconds / 1000} ms')
    num_iter = 50
    times = []
    for i in range(num_iter):
        print(f'[+] Requesting {url} - Iteration {i}', end='\r')
        r = requests.get(url)
        times.append(r.elapsed.microseconds/1000)
        print(f'[+] Request {i} returned {r}              ')
    max_time = max(times)
    min_time = min(times)
    mean_time = sum(times)/len(times)
    print(f'Ritardo massimo {max_time} ms \nRitardo minimo {min_time} ms \nRitardo medio {mean_time} ms')

    plt.hist(times)
    plt.xlabel('Ritardo end-to-end')
    plt.ylabel('Iterazioni')
    plt.title(f'GET requests a {url}')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
