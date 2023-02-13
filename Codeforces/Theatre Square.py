import math

def main():
  n, m, a = map(int, input().split())
  print(math.ceil(n/a)*math.ceil(m/a))

if __name__ == '__main__':
    main()
