# Direct Artifact Download Guide

## ✅ Your Artifacts ARE Available

The GitHub API confirms your artifacts exist and are downloadable. If you're not seeing them in the UI, here are direct download methods.

## Build Run 21865924996 (Feb 10, 2026)

### Artifact 1: SeedSigner OS Image
- **Name:** `seedsigner_os_images-pi0`
- **Size:** 364 MB
- **Artifact ID:** 5449037788
- **Created:** 2026-02-10 13:39:58 UTC
- **Expires:** 2026-05-11 (90 days retention)

### Artifact 2: SHA256 Checksums
- **Name:** `seedsigner_os_images_sha256`
- **Size:** 310 bytes
- **Artifact ID:** 5449044883
- **Created:** 2026-02-10 13:40:26 UTC
- **Expires:** 2026-05-11 (90 days retention)

## Download Methods

### Method 1: Via GitHub Web UI

**Direct Link:** https://github.com/wolverineks/seedsigner/actions/runs/21865924996

1. Open the link above (must be logged into GitHub as @wolverineks)
2. Scroll to the **bottom** of the page
3. Look for the "Artifacts" section (should show 2 items)
4. Click on artifact name to download

**Troubleshooting if not visible:**
- Try refreshing the page (Ctrl+F5 / Cmd+Shift+R)
- Clear browser cache
- Try a different browser or incognito mode
- Check you're logged in as the repo owner

### Method 2: Using GitHub CLI (Recommended)

If the UI isn't showing artifacts, use GitHub CLI:

```bash
# Install gh CLI if needed
# https://cli.github.com/

# Login (if not already)
gh auth login

# Download the OS image artifact
gh run download 21865924996 --name seedsigner_os_images-pi0 --repo wolverineks/seedsigner

# Download the checksums
gh run download 21865924996 --name seedsigner_os_images_sha256 --repo wolverineks/seedsigner

# Or download all artifacts from the run
gh run download 21865924996 --repo wolverineks/seedsigner
```

### Method 3: Direct API Download

Using the API with your personal access token:

```bash
# Set your GitHub token
export GITHUB_TOKEN="your_personal_access_token"

# Download artifact 1 (OS image)
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/wolverineks/seedsigner/actions/artifacts/5449037788/zip \
  -o seedsigner_os_images-pi0.zip

# Download artifact 2 (checksums)
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/wolverineks/seedsigner/actions/artifacts/5449044883/zip \
  -o seedsigner_os_images_sha256.zip
```

## Other Successful Builds

### Build Run 21551315057 (Jan 31, 2026)
- Image: Artifact ID 5330673749 (364 MB)
- Checksums: Artifact ID 5330674628 (309 bytes)
- Link: https://github.com/wolverineks/seedsigner/actions/runs/21551315057

### Build Run 21517762917 (Jan 30, 2026)
- Image: Artifact ID 5319953571 (364 MB)
- Checksums: Artifact ID 5319960489 (309 bytes)
- Link: https://github.com/wolverineks/seedsigner/actions/runs/21517762917

## Verify Downloads

After downloading, extract and verify:

```bash
# Extract the OS image
unzip seedsigner_os_images-pi0.zip

# Extract checksums
unzip seedsigner_os_images_sha256.zip

# Verify the image integrity
sha256sum -c seedsigner_os.*.sha256
```

## Still Having Issues?

If you still cannot access the artifacts after trying these methods, there may be:
1. A GitHub platform issue - check https://www.githubstatus.com/
2. Browser extension blocking content
3. Network/firewall restrictions

The artifacts definitely exist in the system and are accessible via the API.
