from qiskit import QuantumCircuit, Aer, execute

def run_quantum():
    qc = QuantumCircuit(2)

    # Superposición
    qc.h(0)

    # Entrelazamiento
    qc.cx(0, 1)

    qc.measure_all()

    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator).result()

    counts = result.get_counts()

    return counts
