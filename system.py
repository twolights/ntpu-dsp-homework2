import numpy as np


def H1(z: complex) -> complex:
    u1 = 1.0 - 0.98 * np.exp(0.8j * np.pi) / z
    u2 = 1.0 - 0.98 * np.exp(-0.8j * np.pi) / z
    l1 = 1.0 - 0.8 * np.exp(0.4j * np.pi) / z
    l2 = 1.0 - 0.8 * np.exp(-0.4j * np.pi) / z
    return u1 * u2 / (l1 * l2)


def H2(c_k: complex, z: complex) -> complex:
    u1 = np.conj(c_k) - z ** -1
    u2 = c_k - z ** -1
    l1 = 1.0 - c_k * z ** -1
    l2 = 1.0 - np.conj(c_k) * z ** -1
    return (u1 * u2 / (l1 * l2)) ** 2


def c(k: int) -> complex:
    factor = 0.15 * np.pi + 0.02 * np.pi * k
    return 0.95 * np.exp(1j * factor)


def H(z: complex) -> complex:
    result = H1(z)
    for k in range(1, 4 + 1):
        result *= H2(c(k), z)
    return result


def H_of_omega(omega: float) -> complex:
    return H(np.exp(1j * omega))
