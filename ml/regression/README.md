# Regression Analysis with JupyterLab

This directory contains a JupyterLab setup for regression analysis and machine learning experiments.

## Quick Start

### Automated Setup
```bash
python setup.py
```

### Manual Setup
1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start JupyterLab:
   ```bash
   jupyter lab
   ```

## Included Packages

- **JupyterLab**: Modern web-based interactive development environment
- **NumPy**: Fundamental package for scientific computing
- **Pandas**: Data manipulation and analysis library
- **Matplotlib & Seaborn**: Data visualization libraries
- **Scikit-learn**: Machine learning library
- **SciPy**: Scientific computing library
- **Plotly**: Interactive plotting library
- **IPywidgets**: Interactive widgets for Jupyter notebooks

## Usage

Once JupyterLab is running, you can:
- Create new notebooks for regression analysis
- Import and explore datasets
- Build and evaluate regression models
- Visualize data and results
- Export your work

## Directory Structure

```
ml/regression/
├── requirements.txt    # Python dependencies
├── setup.py           # Automated setup script
├── README.md          # This file
├── venv/              # Virtual environment (created after setup)
└── notebooks/         # Your Jupyter notebooks (create as needed)
```

## Tips

- Save your notebooks in a `notebooks/` subdirectory for better organization
- Use meaningful names for your notebook files
- Consider version controlling your notebooks (excluding outputs)
- Use the virtual environment to keep dependencies isolated 