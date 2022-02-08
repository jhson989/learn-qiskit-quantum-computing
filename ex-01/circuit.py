import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

circuit = QuantumCircuit(4, 4)
circuit.x(0)
circuit.h(1)
circuit.h(3)

circuit.measure([0, 1, 2, 3], [0, 1, 2, 3])
circuit.draw(output='mpl', style={'backgroundcolor': '#EEEEEE'}).show()

backend = Aer.get_backend('qasm_simulator')
results = execute(circuit, backend).result()
counts = results.get_counts()

print(counts)
plot_histogram(counts)
plt.show()

