from scipy.interpolate import splrep
from scipy.interpolate import splev
import scipy.interpolate
from numpy import pi

x = np.linspace(0, 6*np.pi, 100)
y = 5 * np.sin(x+pi/3) + 3 * np.random.random(size=x.shape)

plt.plot(x,y, 'o--')

#print(x)
#print(y)

def sin_func(x, a, b):
    y = a * np.sin(x + b) 
    return y

from scipy.optimize import curve_fit

opt, cov = curve_fit(sin_func, x, y)

# fitted data, any number of parameters is allowable
y_fit = sin_func(x, *opt)


rmse = RMSE(y_fit, y)

plt.plot(x, y,     'o',     label='raw data')
plt.plot(x, y_fit, 'r',    label='fit')

plt.legend(loc='best')
plt.title(f'RMSE: {rmse}')

# show the optimised parameters
print(f"y = {opt[0]} * e**({opt[1]}*x)")

z = np.vstack((x,y))

print(z)

#np.savetxt("signal_data.csv", z, delimiter=",")
