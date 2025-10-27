# .\devcontainer\setup2.ps1
Write-Host "Starting configuration..."
# Retrieve the current branch name and trim whitespace.
$currentBranch = (git rev-parse --abbrev-ref HEAD).Trim()
Write-Host "Current branch: $currentBranch"
try {
    $originUrl = git remote get-url origin 2>$null
    if (-not $originUrl) {
        Write-Error "ERROR: 'origin' remote not defined. Please add it."
        exit 1
    }
} catch {
    Write-Error "ERROR: 'origin' remote not defined. Please add it."
    exit 1
}
try {
    $templateUrl = git remote get-url template 2>$null
    if (-not $templateUrl) {
        Write-Error "ERROR: 'template' remote not defined. Please add it."
        exit 1
    }
} catch {
    Write-Error "ERROR: 'template' remote not defined. Please add it."
    exit 1
}
Write-Host "Configuring branch '$currentBranch' to track origin/$currentBranch..."
git branch --unset-upstream $currentBranch 2>$null || $null
git branch --set-upstream-to=origin/$currentBranch $currentBranch

Write-Host "Setting up alias 'pull-template' to fetch and rebase from template/$currentBranch..."
git config --local alias.pull-template "!git fetch template && git rebase template/$currentBranch"

Write-Host "Setting pull strategy to use rebase by default..."
git config --local pull.rebase true

Write-Host "Configuration complete."
exit 0
