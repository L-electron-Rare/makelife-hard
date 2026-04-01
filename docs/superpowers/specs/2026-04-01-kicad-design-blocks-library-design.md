# KiCad Design Blocks Library — Spec

**Date**: 2026-04-01
**Repo**: L-electron-Rare/makelife-hard
**Author**: Clement Saillant / Claude Opus 4.6

## Goal

Extract reusable KiCad design blocks from 15 existing hardware projects into a structured library with custom symbols/footprints, hierarchical sheets, and reference templates. This transforms scattered project-specific schematics into a documented, composable hardware design system.

## Source Projects

| Project | Path | Blocks to Extract |
|---------|------|-------------------|
| BMU Parallelator | `1-KXKM/KXKM_Batterie_Parallelator` | LDO 3.3V/5V, INA237, TCA9535, MOSFET switch, ESP32-S3, IDC, bornier |
| KXKM Audio Board | `1-KXKM/KXKM_ESP32_Audio_Battery_hardware` | Audio codec I2S, battery charger, ESP32-WROOM |
| RJ45-LEDstrip | `1-KXKM/RJ45-LEDstrip` | RJ45 daisy-chain, LED buffer |
| ESP-LED (ANR) | `2-ANR/PCB esp_led` | ESP32 minimal, LED output |
| HypnoLED / DALI PCB | `Fauteuil_Hypnotherapie` | DALI interface, audio-to-LED, MCP power, UI |
| DMX Stepper | `Hemisphere/DMX_ESP_Stepper-controler` | DMX RS-485 receiver, level shifter |
| Orpheo | `Hemisphere/orpheo` | Stepper CL86T driver |
| LEDcurtain | `LEDcurtain_hardware` | Shift register driver, Teensy board |
| Les Amis Nos Morts | `Les_Amis_Nos_Morts` | I2C current control, I2C pot |
| Super Mixer | `Projets_Creatifs/L_Electron_Fou/Super mixer` | Preamp mic/line, EQ 3-band, power +-15V, AUX out |
| Matrix In/Out | `Projets_Creatifs/L_Electron_Fou/matrix in out` | Audio matrix switching |

## Library Structure

```
makelife-hard/
├── library/
│   ├── makelife.kicad_sym
│   ├── makelife.kicad_mod
│   └── makelife.3dshapes/
├── blocks/
│   ├── power/          (3 blocks)
│   ├── mcu/            (2 blocks)
│   ├── sensing/        (3 blocks)
│   ├── protection/     (2 blocks)
│   ├── audio/          (4 blocks)
│   ├── led/            (3 blocks)
│   ├── motor/          (2 blocks)
│   └── connectors/     (3 blocks)
├── templates/          (3 complete assemblies)
├── docs/
└── tools/
```

## Block Inventory (22 blocks, 8 categories)

### power/ — Power Supply
| Block | File | Source | Description |
|-------|------|--------|-------------|
| LDO 3.3V/5V | `ldo-3v3-5v.kicad_sch` | BMU v2 | 24-30V input, dual LDO, bulk caps, protection diode |
| Bipolar +-15V | `supply-bipolar-15v.kicad_sch` | Super Mixer | Dual rail for analog audio, DC-DC or transformer |
| Battery charger | `battery-charger.kicad_sch` | KXKM Audio | Li-ion/LiFePO4 charge IC, status LED |

### mcu/ — Microcontrollers
| Block | File | Source | Description |
|-------|------|--------|-------------|
| ESP32-S3 minimal | `esp32-s3-minimal.kicad_sch` | BMU v2 | ESP32-S3-WROOM + USB-C + boot/reset + flash/PSRAM |
| ESP32-WROOM | `esp32-wroom.kicad_sch` | KXKM Audio / ESP-LED | ESP32-WROOM-32 basique + decoupling |

### sensing/ — Current/Voltage Sensing & I2C
| Block | File | Source | Description |
|-------|------|--------|-------------|
| INA237 current | `ina237-current.kicad_sch` | BMU v2 | INA237 TSSOP-10, shunt resistor, I2C addr config |
| TCA9535 expander | `tca9535-expander.kicad_sch` | BMU v2 | 16-bit I2C GPIO, addr pins, decoupling |
| I2C bus | `i2c-bus.kicad_sch` | BMU v2 | Multi-device I2C, 4.7k pull-ups, dual-bus pattern |

### protection/ — Battery & Power Protection
| Block | File | Source | Description |
|-------|------|--------|-------------|
| MOSFET switch | `mosfet-switch.kicad_sch` | BMU v2 | N-channel MOSFET, gate driver, flyback diode |
| Reverse protection | `reverse-protection.kicad_sch` | BMU v2 | P-MOSFET reverse polarity, TVS |

### audio/ — Audio Processing
| Block | File | Source | Description |
|-------|------|--------|-------------|
| Preamp mic/line | `preamp-mic-line.kicad_sch` | Super Mixer | Differential preamp, phantom power option, gain pot |
| EQ 3-band | `eq-3band.kicad_sch` | Super Mixer | Bass/mid/treble active EQ, op-amp based |
| Audio codec I2S | `audio-codec-i2s.kicad_sch` | KXKM Audio | I2S codec (e.g. ES8388/WM8960), MCLK, headphone out |
| Audio to LED | `audio-to-led.kicad_sch` | HypnoLED | Envelope follower, peak detect, LED PWM output |

### led/ — LED Drivers
| Block | File | Source | Description |
|-------|------|--------|-------------|
| Shift register driver | `led-driver-shift.kicad_sch` | LEDcurtain | 74HC595 or similar, cascadable, constant current |
| Level shifter | `level-shifter.kicad_sch` | DMX Stepper | 3.3V to 5V bidirectional, MOSFET or 74HCT |
| DALI interface | `dali-interface.kicad_sch` | HypnoLED | DALI bus transceiver, galvanic isolation |

### motor/ — Motor Control
| Block | File | Source | Description |
|-------|------|--------|-------------|
| DMX input | `dmx-input.kicad_sch` | DMX Stepper | RS-485 receiver (MAX485), XLR-5 connector |
| Stepper driver | `stepper-driver.kicad_sch` | Orpheo | CL86T interface, step/dir/enable, optocoupler |

### connectors/ — Interconnect
| Block | File | Source | Description |
|-------|------|--------|-------------|
| IDC bus | `idc-bus.kicad_sch` | BMU v2 | IDC-10/16 ribbon cable, pinout standard |
| RJ45 daisy-chain | `rj45-daisy.kicad_sch` | RJ45-LEDstrip | Dual RJ45 in/out, pin mapping for data + power |
| Bornier 24V | `bornier-24v.kicad_sch` | BMU v2 | Screw terminal, wire gauge annotation, fuse holder |

## Templates (3 assemblies)

| Template | Blocks Used | Purpose |
|----------|-------------|---------|
| `bmu-complete/` | power/ldo + sensing/ina237 + sensing/tca9535 + sensing/i2c-bus + protection/mosfet + mcu/esp32-s3 + connectors/idc + connectors/bornier | Full BMU — proves all blocks assemble |
| `led-controller/` | power/ldo + mcu/esp32-wroom + led/shift-register + led/level-shifter + connectors/rj45-daisy | LED strip controller |
| `audio-processor/` | power/bipolar-15v + mcu/esp32-wroom + audio/preamp + audio/eq-3band + audio/codec-i2s | Audio processing board |

## Block Interface Convention

Every hierarchical sheet exposes:
- **Power labels**: `VIN`, `3V3`, `5V`, `GND`, `V+`, `V-` (as applicable)
- **Signal labels**: `SDA`, `SCL`, `MOSI`, `MISO`, `SCK`, `TX`, `RX`, `DMX_IN` etc.
- **Hierarchical pins**: Named with prefix matching the block category (e.g. `BATT_SW_OUT`, `INA_ALERT`)
- **Text annotations**: Critical constraints on the schematic (e.g. "Pull-ups 4.7k required", "Topology: TCA*4 = INA")

## Custom Symbols

Extracted from source projects into `makelife.kicad_sym`:
- INA237 (TSSOP-10) — from BMU v2
- TCA9535 (TSSOP-24) — from BMU v2
- Custom MOSFET packages used in BMU
- CL86T stepper driver connector — from Orpheo
- DALI transceiver — from HypnoLED
- Audio codec IC (ES8388 or WM8960) — from KXKM Audio

## Documentation

### `docs/catalog.md`
Index of all blocks with:
- Category, name, 1-line description
- Source project reference
- Interface pins list
- Critical design constraints

### `docs/design-rules.md`
Per-domain rules:
- Power: max current per trace, thermal relief, decoupling placement
- I2C: pull-up values by bus speed (100kHz/400kHz), max capacitance
- Battery: MOSFET Rds(on), gate charge, protection timing
- Audio: ground plane strategy, analog/digital separation
- LED: current limiting, thermal, EMC
- Motor: isolation requirements, flyback protection

### `docs/sources.md`
Traceability: each block maps to its source project, original file path, and any modifications made during extraction.

## Tooling

### `tools/validate_drc.py`
- Runs `kicad-cli sch erc` on all blocks
- Runs `kicad-cli pcb drc` on templates
- CI integration via GitHub Actions

### `tools/export_gerber.py`
- Exports Gerber + drill + BOM + pick-and-place for templates
- Uses KiBot configuration

## Out of Scope

- No PCB layouts for individual blocks (blocks are schematic-only, reusable as hierarchical sheets)
- No 3D models creation (only referencing existing STEP files from source projects)
- No simulation (SPICE models are referenced but not validated)
- No firmware in this repo (that's makelife-firmware)

## Success Criteria

1. All 22 blocks pass ERC with 0 errors
2. All 3 templates assemble and pass ERC+DRC
3. `docs/catalog.md` lists every block with complete interface description
4. CI runs `validate_drc.py` on push
