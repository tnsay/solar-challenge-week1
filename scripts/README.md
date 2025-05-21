"# scripts README" 
# Project Name

 This project aims to identify the most suitable country—Benin, Sierra Leone, or Togo—for setting up a solar farm based on there data available and showcasing a dashboard for simple review.

## Development Process
-perform EDA on separate branch for countries
- Created separate Git branches for each country dataset (`benin-eda`, `serria-leon-eda`, `togo-eda`).
-do comparision on separate branch-compare-countries
- Developed main dashboard features in branch `dashboard-dev`.
- Used Python 3.9+ and Streamlit for the frontend.
- Data cleaning scripts are located in `notebooks/` folder.
- Visualizations include boxplots, summary tables by region, etc.

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/tnsay/solar-challenge-week1.git
   cd solar-challenge-week1

 ## run streamlite dashboard 
 streamlit run app/main.py
  