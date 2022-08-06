# Pearson Correlation Coefficient 1

n = int(input())
x = list(map(float,input().strip().split()))
y = list(map(float,input().strip().split()))

mean_x = sum(x) / n
mean_y = sum(y) / n

std_x = (sum([(i - mean_x)**2 for i in x]) / n)**0.5
std_y = (sum([(j - mean_y)**2 for j in y]) / n)**0.5

covariance = sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(n)])

correlation_coeff = covariance / (n * std_x * std_y)

print(round(correlation_coeff,3))

