# SeedSigner Build Artifacts

## Latest Successful Build

**Build Run:** 21865924996  
**Date:** February 10, 2026 at 13:01 UTC  
**Status:** ✅ Success  
**Branch:** dev

### Available Artifacts

1. **seedsigner_os_images-pi0** (364 MB)
   - Contains the bootable .img.zip file for Raspberry Pi Zero
   - Download: https://github.com/wolverineks/seedsigner/actions/runs/21865924996

2. **seedsigner_os_images_sha256** (310 bytes)
   - Contains SHA256 checksums for verification
   
### How to Download

1. Go to: https://github.com/wolverineks/seedsigner/actions/runs/21865924996
2. Scroll down to the "Artifacts" section at the bottom
3. Click on "seedsigner_os_images-pi0" to download
4. Extract the .img.zip file
5. Use a tool like Balena Etcher or Raspberry Pi Imager to flash to SD card

## Recent Build Failures

Recent builds have been failing due to Docker build errors in the seedsigner-os build process. The builds are attempting to pull from:
- App: `3rdIteration/seedsigner@dev`
- OS: `3rdIteration/seedsigner-os@main`

The Docker container exits with code 2 before producing image files.

## Triggering a New Build

To trigger a manual build, go to:
https://github.com/wolverineks/seedsigner/actions/workflows/build.yml

Click "Run workflow" and adjust parameters as needed.
