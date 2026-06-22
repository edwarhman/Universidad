import numpy as np
import matplotlib.pyplot as plt

r0 = 1.0
theta = np.linspace(0, 4 * np.pi, 1000)
r = r0 * np.exp(theta)

x = r * np.cos(theta)
y = r * np.sin(theta)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(x, y, "b-", linewidth=1.5)
ax1.scatter([x[0]], [y[0]], color="red", zorder=5, label=f"Inicio θ=0")
ax1.scatter([x[-1]], [y[-1]], color="green", zorder=5, label=f"Final θ={theta[-1]:.1f}")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title(f"Trayectoria: $r(\\theta) = r_0 e^{{\\theta}}$ (espiral logarítmica)")
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_aspect("equal")

ax2.plot(theta, r, "r-", linewidth=1.5)
ax2.set_xlabel("θ [rad]")
ax2.set_ylabel("r(θ)")
ax2.set_title("Radio en función del ángulo")
ax2.grid(True, alpha=0.3)

plt.tight_layout()
print("Mostrando gráfica...")
plt.show()
