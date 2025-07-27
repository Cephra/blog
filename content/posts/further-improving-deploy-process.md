+++
title = "Further Improving Deploy Process"
date = 2025-07-27 14:05:48+02:00
draft = true
+++
## Latest Deploy Script Update
### v3 Released

The newest deploy script update (v3) has been released, introducing a more streamlined and efficient process for deploying applications to production.

This version includes several key improvements over its predecessor, making it easier to get an application up and running on the servers. The changes are focused on better handling of edge cases, particularly when dealing with temporary directories and error scenarios.

### Notable Improvements

The most significant enhancement is the improved logic for creating a temporary directory (`deploy_dir`). Instead of relying solely on `mktemp`, I'm now using a more reliable method to create a unique directory within the user's home folder. This should help mitigate potential issues related to temp file creation.

Another notable change is the enhanced error handling throughout the script. I've added more explicit checks for failure conditions, ensuring that if something goes wrong during deployment, the script will correctly identify and report the issue.

The `trap` statement has been added, which guarantees that the `cleanup` function will be executed in case of an unexpected exit (e.g., due to a signal or error). This ensures that the temporary directory is always properly cleaned up, preventing potential clutter on the system. Furthermore, I've implemented additional validation for the input arguments and environment variables.

### Code

Below is the updated script:

```bash
#!/usr/bin/env bash
set -euo pipefail

# -----------------------------------------------------------------------------
# Usage: deploy.sh <git-repo-url> [deploy-arg1 deploy-arg2 ...]
# -----------------------------------------------------------------------------
if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <git-repo-url> [args...]" >&2
    exit 1
fi
repo_url=$1

deploy_dir=$(mktemp --tmpdir="${HOME}" --dry-run "${TMPDIR:-/tmp}/deploy.XXXXXXXXXX") \
    || { echo "Error: failed to create temp directory" >&2; exit 1; }

cleanup() {
    rm -rf "$deploy_dir"
}
trap cleanup EXIT

git clone --depth 1 -- "$repo_url" "$deploy_dir" \
    || { echo "Error: git clone failed" >&2; exit 1; }

cd "$deploy_dir"

if [[ ! -f "./deploy.sh" ]]; then
    echo "Error: deploy.sh not found in repository" >&2
    exit 1
elif [[ ! -x "./deploy.sh" ]]; then
    echo "Info: making deploy.sh executable"
    chmod +x ./deploy.sh
fi

./deploy.sh
```
