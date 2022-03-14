import requests
from matplotlib import pyplot as plt
import sys

INFO = '\u001b[34m\u001b[1m[+]\u001b[0m'
ERROR = '\u001b[31m\u001b[1m[!]\u001b[0m'

def main():
    url = 'http://127.0.0.1:8000'
    
    num_iter = int(sys.argv[1])
    
    times = []
    print(f'{INFO} Requesting {url}')
    for i in range(num_iter):
        print(f'{INFO} Requesting {url} - Iteration {i}', end='\r')
        try:
            r = requests.get(url)
            times.append(r.elapsed.microseconds/1000)

            if(r.status_code != 200):
                raise ConnectionError
            print(f'{INFO} Request {i} returned {r.status_code} - Delay: {r.elapsed.microseconds/1000} ms {" "*20}')
        except ConnectionError:
            print(f'{ERROR} Request {i} returned {r.status_code}{" "*70}')
            break

    plt.plot(times, label=url.rsplit('/', 1)[1])

    plt.ylabel('Delays end-to-end')
    plt.xlabel('Iteration')
    plt.title(f'GET requests')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
