# Seedsigner (react-native inspired ui code)

## Intentions
- declarative components
- unidirectional data flow
- familiar router/navigation
- business logic / ui separation (client/server-ish)

## Todo
- [x] buttons
- [x] basic text
- [x] backgrounds
- [x] render cycle
- [x] paint on desktop
- [x] toast notification
- [x] user inputs on desktop
- [x] router navigation
- [x] async example (toast notification) 
- [ ] paint on rpi
- [ ] perf test rpi
- [x] scrollable list
- [ ] camera
- [x] icons
- [ ] fonts
- [x] settings in memory
- [ ] better types
- [ ] better imports
- [ ] more screens

# Screens
- [x] Main Menu

- [ ] **Power Screens**
  - [x] Power Options
  - [x] Restart
  - [x] Power Off

- [ ] **Seed Screens**
  - [x] Seeds Menu (index)
  - [ ] Load Seed (new)
    - [ ] Seed Mnemonic Entry
    - [ ] Seed Mnemonic Invalid
    - [ ] Seed Mnemonic Finalize
    - [ ] **Seed Passphrase Entry**
      - [ ] Alpha Keyboard
      - [ ] Numeric Entry
      - [ ] Symbols1 Entry
      - [ ] Symbols2 Entry
      - [ ] Discard Passphrase
  - [ ] Verify Passphrase (create)
  - [ ] Seed Options (show)
    - [ ] **Export Xpub**
        - [ ] Export Options
        - [ ] Export Derivation Path
        - [ ] Export Coordinator
    - [ ] **Backup Seed**
      - [ ] Backup Seed Options
        - [ ] Seed Export
          - [ ] Seed Export Warning
          - [ ] Seed Export Details
          - [ ] Seed Words Warning
          - [ ] Seed Words
          - [ ] BIP-85
          - [ ] BIP-85 Index
          - [ ] BIP-85 Index Invalid

- [ ] **PSBT Screens**

- [ ] **Tools Screens**
  - [x] Tools Menu
    - [ ] Mnemonic Length Camera
    - [ ] Mnemonic Length Dice
    - [ ] Dice Entry
  - [ ] Calc 12th/24th Word
  - [ ] **Address Explorer**
    - [ ] Select Seed
    - [ ] Select Address Type
    - [ ] Addresses List


- [ ] **Settings Screens**
  - [x] Settings Menu
  - [x] Language
  - [x] Persistent Settings
  - [x] Coordinator
  - [x] Display Denomination
  - [ ] Advanced Settings Menu
    - [ ] Network
    - [ ] QR Code Density
    - [ ] Xpub export
    - [ ] Sig Types
    - [ ] Script Types
    - [ ] View Xpub
    - [ ] BIP-39
    - [ ] Camera Rotation
    - [ ] Compact SeedQR
    - [ ] BIP-85
    - [ ] Electrum Seeds
    - [ ] Privacy Warnings
    - [ ] Dire Warnings
    - [ ] QR Brightness Tips
    - [ ] Partner Logos
    - [ ] **Hardware**
      - [ ] Display Type
      - [ ] Invert Colors
  - [ ] IO Test
  - [ ] Donate
  - [ ] Noob Mode
  - [ ] Ephemeral Mode

- [ ] **Error Screens**
  - [ ] Work In Progress
  - [ ] System Error
  - [ ] Network Mismatch
  - [ ] Option Disabled
  - [ ] Scan Invalid

## Maybe Todo
- [ ] nested routing
- [ ] load settings from disk
- [ ] do actual bitcoin stuff
- [ ] testing