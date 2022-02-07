# Q3
import numpy as np

xy = np.array([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0], [12.0, 22.0, 32.0, 42.0, 52.0, 62.0]])

x_train = xy[0]
y_train = xy[1]

print("\n==========Q3==========")
print(x_train, x_train.shape)
print(y_train, y_train.shape)

# Q4

beta_gd = np.random.rand(1)
bias = np.random.rand(1)

print("\n==========Q4==========")
print(beta_gd, bias)

# Q5

learning_rate = 0.01
n = 6

for i in range(1001):
    pred = (x_train * beta_gd) + bias
    error = ((y_train - pred) ** 2).mean()

    grad_beta = (-2) * (np.transpose(x_train) @ (y_train - pred)).mean()
    grad_bias = (-2) * (y_train - pred).mean()

    beta_gd -= learning_rate * grad_beta
    bias -= learning_rate * grad_bias

    if i % 100 == 0:
        print(
            "Epoch ({:10d}/1000) error: {:10f}, beta_gd: {:10f}, bias:{:10f}".format(
                i, error, beta_gd.item(), bias.item()
            )
        )

