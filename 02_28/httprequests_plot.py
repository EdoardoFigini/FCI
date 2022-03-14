import requests
from matplotlib import pyplot as plt


def main():
    url = 'http://www.google.com'
    #print(r.text)
    #print(f'Ritardo: {r.elapsed.microseconds / 1000} ms')
    num_iter = 10
    times = []
    for i in range(num_iter):
        r = requests.get(url)
        times.append(r.elapsed.microseconds/1000)
    print(r)
    max_time = max(times)
    min_time = min(times)
    mean_time = sum(times)/len(times)
    print(f'Ritardo massimo {max_time} ms \nRitardo minimo {min_time} ms \nRitardo medio {mean_time} ms')


if __name__ == '__main__':
    main()
