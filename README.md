# dev-tool-testing

## Using Black

To run `black` on a single file, we can do:

```bash
black single_python_file.py
```

which will automatically write the necessary formatting changes directly to the file. To do a "dry run" and see the effect of the formatting changes without altering the file itself, do:

```bash
black --diff single_python_file.py
```

To format all the Python files (or check all the files) in the current directory, do:

```bash
black .
```


## Run Black Automatically Before Committing

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

4. To test it, try to commit a new file or modify an existing file with formatting problems (for example, a line of code longer than 88 characters). Add this file to the staging area, `git add modified_file.py`, and then commit it, `git commit -m "add a too long line"`. If configured correctly, you should see something like the following:

	```bash
	(pvade) [conda-arm] eyoung$ git commit -m "add a too long line"
	black....................................................................Failed
	- hook id: black
	- files were modified by this hook

	reformatted modified_file.py

	All done! ✨ 🍰 ✨
	1 file reformatted.
	```

	where `black` has alerted you to the fact that formatting changes were necessary. To proceed with the commit, *you must re-add the formatted file to the staging area*, `git add modified_file.py`, then again commit it `git commit -m "add a too long line"`, which should result in something like:

	```bash
	(pvade) [conda-arm] eyoung$ git commit -m "add a too long line"
	black....................................................................Passed
	[main 013b033] add a too long line
	1 file changed, 4 insertions(+)
	```

