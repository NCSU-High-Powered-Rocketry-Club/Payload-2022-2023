import matplotlib.pyplot as plt
from rtlsdr import RtlSdr

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.4e6
sdr.center_freq = 900e6
sdr.gain = 4

samples = sdr.read_samples(128*1024)
sdr.close()

# use matplotlib to estimate and plot the PSD
plt.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
plt.xlabel('Frequency (MHz)')
plt.ylabel('Relative power (dB)')

plt.savefig("delete_this.png")
