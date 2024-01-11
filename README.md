# dev-tool-testing

0. These instructions assume you have an active Conda environment built for `PVAde` which contains the `black` package for code formatting. If not, build a minimal Conda environment with `black` and `numpy` to follow along.

1. Activate your Conda environment and install the pre-commit package:

	```bash
	pip install pre-commit
	``` 

2. Define the `.pre-commit-config.yaml` file at the root of the repo (this step is already done here)

3. Install the pre-commit hooks in your .git/ directory:

	```bash
	pre-commit install
	``` 
