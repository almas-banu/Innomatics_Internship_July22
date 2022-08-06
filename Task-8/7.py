# The Central Limit Theorem 3

#sample size
n = int(input())

#population parameters
mean = int(input())
std = int(input())

#distribution
dis = float(input())

#z-score 
z = float(input())

# sample mean and std
mu, sigma = mean, std/(100**0.5)

a = mu - (z*sigma)
b = mu + (z*sigma)

print(round(a,2))
print(round(b,2))