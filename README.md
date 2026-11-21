# fc-agents-sample

> **Disclaimer: this repository is a test fixture for a security lab. It contains known vulnerabilities on purpose.**
> The dependencies in `requirements.txt` have published CVEs, `app.py` has dangerous code patterns, the `Dockerfile`
> runs as root, and the git history holds a fake API token. Nothing here is meant to be installed, run, deployed or
> copied into a real project. Use it only as input for the scanners in the lab below, inside the lab's isolated microVM.

Part of the **DevOps Training** course on YouTube: https://www.youtube.com/@Full-DevOps-Training

A small repository with **planted problems**, for the Firecracker lab *Run AI Agents in Isolated MicroVMs*, Part 3
(https://github.com/elevy99927/aws/tree/main/6-advanced-labs/01-firecracker-agent-sandbox/part-3-three-agents).
Three scanners run on it inside a microVM: Trivy, Semgrep and Gitleaks. Nothing here is real: the token is a random
string that was committed and then removed (so it only lives in the git history), and the dependencies are old on purpose.

| File | What's planted | Found by |
|---|---|---|
| `requirements.txt` | old versions of `requests`, `pyyaml` and `flask` with known CVEs | Trivy (vuln) |
| `Dockerfile` | runs as root, no `USER` | Trivy (misconfig) |
| `app.py` | `eval` on user input, a shell command built from user input, code decoded from base64 and executed | Semgrep |
| `package.json` | a `postinstall` script | Semgrep (a course rule) |
| `config.py` in the first commit | a fake API token | Gitleaks (the history) |

Do not run `app.py`. It is a sample for scanners, not an application.

Test pull request for Part 4 of the Firecracker lab: the webhook starts the scan.
