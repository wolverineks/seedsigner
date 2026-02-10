# Quick Start: Getting a SeedSigner Image

## 🚀 Fastest Solution (Recommended)

### Download Official Pre-Built Image

Go to the official SeedSigner releases page:
👉 **https://github.com/SeedSigner/seedsigner/releases/latest**

1. Download the `.img` file for your Raspberry Pi model:
   - Pi Zero/Pi Zero W: `seedsigner_os.0.8.6.pi0.img`
   - Pi Zero 2 W: `seedsigner_os.0.8.6.pi02w.img`
   - Pi 4: `seedsigner_os.0.8.6.pi4.img`

2. Flash to SD card using:
   - **Balena Etcher** (https://www.balena.io/etcher/)
   - **Raspberry Pi Imager** (https://www.raspberrypi.com/software/)

3. Insert SD card into your Raspberry Pi and power on!

## Why Can't I See Artifacts Here?

GitHub Actions artifacts are **only visible to repository collaborators**. Even though this repository is public, the build artifacts are restricted.

## Alternative: Build Your Own

If you want to build from this fork:

1. Fork this repository to your GitHub account
2. Go to **Actions** → **Build** workflow
3. Click **Run workflow** 
4. Wait ~30-40 minutes
5. Download artifacts from YOUR workflow run (they'll be visible to you)

---

📖 **See BUILD_ARTIFACTS.md for detailed information**
