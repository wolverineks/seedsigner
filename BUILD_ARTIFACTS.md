# SeedSigner Build Artifacts

## ⚠️ Important: Artifact Access

**GitHub Actions artifacts are only visible to repository collaborators.** If you don't have direct access to this repository, you won't see the Artifacts section on workflow run pages.

## Solutions to Get a Build

### Option 1: Use Official SeedSigner Releases (Recommended)

The official SeedSigner project provides pre-built, verified images:

**Download from:** https://github.com/SeedSigner/seedsigner/releases/latest

- Latest stable release: v0.8.6
- Images available for all Raspberry Pi models
- Includes SHA256 checksums and GPG signatures
- Thoroughly tested and community verified

### Option 2: Trigger Your Own Build

If you need a custom build from this fork:

1. **Fork this repository** to your own GitHub account
2. Go to **Actions** tab in your fork
3. Select the **Build** workflow
4. Click **Run workflow**
5. Configure build parameters (or use defaults)
6. Wait for build to complete (~30-40 minutes)
7. Download artifacts from your own workflow run

### Option 3: Request Access

If you need artifacts from this specific repository, request collaborator access from the repository owner (@wolverineks).

## Latest Build Status

**Build Run:** 21865924996  
**Date:** February 10, 2026 at 13:01 UTC  
**Status:** ✅ Success (artifacts available to repo collaborators only)  
**Branch:** dev

## Known Build Issues

Recent builds have been failing due to a configuration error in the external `3rdIteration/seedsigner-os` repository:

**Error:** `../pi0-dev/board/genimage-rpi-seedsigner.cfg:21: no such option 'image'`

This is a syntax error in the upstream genimage configuration file and cannot be fixed from this repository. Until the upstream issue is resolved:
- Use the official SeedSigner releases (Option 1 above)
- Or wait for the upstream fix and trigger a new build

## Building Locally

For advanced users who want complete control:

```bash
# Clone the official SeedSigner OS builder
git clone https://github.com/SeedSigner/seedsigner-os.git
cd seedsigner-os

# Follow build instructions
# See: https://github.com/SeedSigner/seedsigner-os/blob/main/docs/building.md
```

This gives you a reproducible build you can verify yourself.
