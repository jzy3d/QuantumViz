E1_electronVolt = 3.14  # eV
E2_electronVolt = 0.36  # eV
lambd1 = 253.7 * 10**(-9)  # nm
lambd2 = 589 * 10**(-9)  # nm

celerity = 299792458  # m/s

def electronVolt_to_joule(electronVolt):
    joule = 10**19 * electronVolt / 1.6
    print(joule)
    return joule



def h(energy, lambd):
    return energy * lambd / celerity


def spatial_frequency(wavelength):
    celerity / wavelength


if __name__ == '__main__':
    E1 = electronVolt_to_joule(E1_electronVolt)
    E2 = electronVolt_to_joule(E2_electronVolt)

    print(E1)
    print("h for E1")
    print(h(E1, lambd1))
