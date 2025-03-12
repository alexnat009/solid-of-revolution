# Solid of Revolution Visualization and Volume Calculation

This project provides tools for visualizing solids of revolution and calculating their volumes using exact and approximate methods. It includes:
- **3D plotting** of solids of revolution around various axes
- **Exact volume computation** using symbolic integration
- **Approximate volume computation** using Simpson's rule

## Features
- **Plot solids of revolution** around the x-axis, y-axis, or custom lines.
- **Compute exact volume** of the solid using SymPy.
- **Estimate volume** with numerical integration (Simpson's rule).
- **Generate animated GIFs** to visualize the revolution process.

## Dependencies
- `numpy`
- `matplotlib`
- `sympy`
- `gif`
- `opencv-python` (if additional image processing is needed)

## Usage

### Exact Volume Calculation
```python
x = sym.Symbol('x', real=True)
volume = exact_volume_of_solid_revolution(sym.Abs(x), -1, 1, (1, 4))
print(volume)
```

### Approximate Volume Calculation
```python
approx_volume = approximate_volume_of_solid_revolution(sym.sin(x) + x**2, 0, 1, (2, 2), 6)
print(approx_volume)
```

### Plot Solid of Revolution
```python
plot_solid_of_revolution(lambda x: x**3, -2, 2, 2*np.pi, display=True)
```

### Generate GIF Animation
```python
frames = []
for i in np.linspace(0, 2 * np.pi, 10):
    frame = plot_solid_of_revolution(lambda x: np.sin(x) + x**2, -3, 3, i)
    frames.append(frame)

gif.save(frames, 'images/vol3.gif', duration=500)
```

## Limitations
- Assumes functions are well-behaved for integration and visualization.
