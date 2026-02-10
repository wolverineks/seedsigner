# SeedSigner Build Artifacts

## ✅ Artifacts ARE Available

**Repository Owner Note:** Your build artifacts exist and are accessible. If you're not seeing them in the GitHub UI, see `ARTIFACT_DOWNLOAD.md` for alternative download methods including GitHub CLI and direct API access.

## Latest Successful Builds

### Build #18 - Run 21865924996 (Feb 10, 2026)
- **Status:** ✅ Success
- **Artifacts:** 2 files (364 MB total)
- **Direct Link:** https://github.com/wolverineks/seedsigner/actions/runs/21865924996
- **Created:** 2026-02-10 13:39 UTC
- **Expires:** 2026-05-11 (90 day retention)

**Quick Download:**
```bash
gh run download 21865924996 --repo wolverineks/seedsigner
```

### Build #3 - Run 21551315057 (Jan 31, 2026)
- **Status:** ✅ Success
- **Direct Link:** https://github.com/wolverineks/seedsigner/actions/runs/21551315057

### Build #1 - Run 21517762917 (Jan 30, 2026)
- **Status:** ✅ Success
- **Direct Link:** https://github.com/wolverineks/seedsigner/actions/runs/21517762917

## Alternative Sources

### Official SeedSigner Releases (Stable)

The official SeedSigner project provides pre-built, verified images:

**Download from:** https://github.com/SeedSigner/seedsigner/releases/latest

- Latest stable release: v0.8.6
- Images available for all Raspberry Pi models
- Includes SHA256 checksums and GPG signatures
- Thoroughly tested and community verified

## Troubleshooting Artifact Visibility

If you can't see artifacts in the GitHub Actions UI:

1. **Refresh the page** - Hard refresh with Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)
2. **Clear browser cache** - Sometimes old cache prevents UI updates
3. **Try different browser** - Or use incognito/private mode
4. **Use GitHub CLI** - Most reliable method (see ARTIFACT_DOWNLOAD.md)
5. **Check GitHub Status** - Visit https://www.githubstatus.com/

The artifacts exist in the system (verified via API) even if the UI doesn't display them.

## Triggering New Builds

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
