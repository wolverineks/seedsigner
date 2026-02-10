# Quick Start: Getting a SeedSigner Image

## 🎯 For Repository Owner

**Your build artifacts ARE available!** See `ARTIFACT_DOWNLOAD.md` for direct download methods if you're having UI issues.

**Quick download via GitHub CLI:**
```bash
gh run download 21865924996 --repo wolverineks/seedsigner
```

## 🚀 Alternative: Official SeedSigner Release

For a tested, verified, production-ready image:

👉 **https://github.com/SeedSigner/seedsigner/releases/latest**

1. Download the `.img` file for your Raspberry Pi model:
   - Pi Zero/Pi Zero W: `seedsigner_os.0.8.6.pi0.img`
   - Pi Zero 2 W: `seedsigner_os.0.8.6.pi02w.img`
   - Pi 4: `seedsigner_os.0.8.6.pi4.img`

2. Flash to SD card using:
   - **Balena Etcher** (https://www.balena.io/etcher/)
   - **Raspberry Pi Imager** (https://www.raspberrypi.com/software/)

3. Insert SD card into your Raspberry Pi and power on!

## Triggering a New Build

To create a fresh build:

1. Go to **Actions** → **Build** workflow
2. Click **Run workflow** 
3. Configure parameters (or use defaults)
4. Wait ~30-40 minutes
5. Download artifacts from the completed run

**Note:** Recent builds may fail due to upstream genimage config error in `3rdIteration/seedsigner-os`.

---

📖 **See ARTIFACT_DOWNLOAD.md for detailed download methods**  
📖 **See BUILD_ARTIFACTS.md for build troubleshooting**
