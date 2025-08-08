# Descriptive Statistics with IMDb Movie Data

[![Codespaces Prebuilds](https://github.com/4GeeksAcademy/perdrizet-descriptive-statistics-exercises-project-with-python/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/4GeeksAcademy/perdrizet-descriptive-statistics-exercises-project-with-python/actions/workflows/codespaces/create_codespaces_prebuilds)

A comprehensive data science project focused on descriptive statistics analysis using Python and Pandas. This project demonstrates essential statistical analysis techniques through practical exercises with real-world IMDb movie data.

![Project Preview](assets/preview.jpeg)


## Project Overview

This project analyzes IMDb movie data to demonstrate fundamental descriptive statistics concepts. The dataset contains 1000 popular movies from the IMDb website and provides hands-on experience with:

- Central tendency measures (mean, median, mode)
- Measures of spread (range, variance, standard deviation)  
- Distribution shape analysis (skewness, kurtosis)
- Manual statistical calculations
- Data visualization and interpretation
- Extreme value identification


## Getting Started

### Option 1: GitHub Codespaces (Recommended)

1. **Fork the Repository**
   - Click the "Fork" button on the top right of the GitHub repository page
   - 4Geeks students: set 4GeeksAcademy as the owner - 4Geeks pays for your codespace usage. All others, set yourself as the owner
   - Give the fork a descriptive name. 4Geeks students: I recommend including your GitHub username to help in finding the fork if you lose the link
   - Click "Create fork"
   - 4Geeks students: bookmark or otherwise save the link to your fork

2. **Create a GitHub Codespace**
   - On your forked repository, click the "Code" button
   - Select "Create codespace on main"
   - If the "Create codespace on main" option is grayed out - go to your codespaces list from the three-bar menu at the upper left and delete an old codespace
   - Wait for the environment to load (dependencies are pre-installed)

3. **Start Working**
   - Open `notebooks/assignment.ipynb` in the Jupyter interface
   - Follow the step-by-step instructions in the notebook

### Option 2: Local Development

1. **Prerequisites**
   - Git
   - Python >= 3.10

2. **Fork the repository**
   - Click the "Fork" button on the top right of the GitHub repository page
   - Optional: give the fork a new name and/or description
   - Click "Create fork"

3. **Clone the repository**
   - From your fork of the repository, click the green "Code" button at the upper right
   - From the "Local" tab, select HTTPS and copy the link
   - Run the following commands on your machine, replacing `<LINK>` and `<REPO_NAME>`

   ```bash
   git clone <LINK>
   cd <REPO_NAME>
   ```

4. **Set Up Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Launch Jupyter & start the notebook**
   ```bash
   jupyter notebook notebooks/assignment.ipynb
   ```


## Project Structure

```
├── .devcontainer/        # Development container configuration
├── assets/               # Images and resources directory
│   ├── distribution.png  # Distribution visualization examples
│   ├── preview.jpeg      # Project preview image
│   └── quantiles.png     # Quantiles visualization examples
│
├── data/                 # Data file directory
│   └── imdb_1000.csv     # IMDb movie dataset
│
├── notebooks/            # Jupyter notebook directory
│   ├── assignment.ipynb  # Assignment notebook (student version)
│   ├── solution.ipynb    # Solution notebook (complete analysis)
│   └── functions.py      # Helper functions module
│
├── tests/                # Unit tests directory
│   └── test_functions.py # Tests for helper functions
│
├── .gitignore            # Files/directories not tracked by git
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```


## Dataset

The dataset (`data/imdb_1000.csv`) contains 1000 popular movies from IMDb with the following features:
- **title**: Movie titles (primary focus for statistical analysis)
- **star_rating**: IMDb ratings (1-10 scale)
- **content_rating**: Age-appropriate ratings (G, PG, PG-13, R, etc.)
- **genre**: Movie genres (Action, Comedy, Drama, etc.)
- **duration**: Movie length in minutes
- **actors_list**: List of main actors

**Note**: This dataset was collected for educational purposes only. Focus is primarily on analyzing title length characteristics using descriptive statistics.


## Learning Objectives

1. **Statistical Measures**: Understanding and applying descriptive statistics
2. **Data Analysis**: Extracting insights from numerical data
3. **Manual Calculations**: Building intuition through step-by-step computation
4. **Data Visualization**: Creating meaningful plots and interpretations
5. **Python Programming**: Using pandas, numpy, scipy, and matplotlib


## Technologies Used

- **Python 3.11**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing and array operations
- **SciPy**: Statistical functions (skewness, kurtosis, mode)
- **Matplotlib**: Data visualization and plotting
- **Jupyter**: Interactive development environment


## Contributing

This is an educational project. Contributions for improving the analysis or adding new statistical insights are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request
