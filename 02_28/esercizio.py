import requests
from matplotlib import pyplot as plt


def media(l: list) -> float:
    return sum(l)/len(l)


def main():
    urls = ['http://www.google.com',
            'http://www.youtube.com',
            'http://www.polimi.it',
            'http://www.wikipedia.org',
            'http://www.amazon.com',
            'http://www.twitter.com']
    
    best_time=100000
    best_url = ''
    for url in urls:
        times = [requests.get(url).elapsed.microseconds/1000 for _ in range(6)]
        avg_time = media(times)
        print(f'Response from {url}\t-   Average response time: {avg_time}')
        if(avg_time<best_time):
            best_time = avg_time
            best_url = url
        plt.plot(times, label=url.rsplit('/', 1)[1])
    
    print(f'Best Response time (on average): {best_url} -> {best_time}')

    plt.ylabel('Delay end-to-end')
    plt.xlabel('Iterations')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
