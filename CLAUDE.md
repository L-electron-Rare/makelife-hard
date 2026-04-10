# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Context

makelife-hard is the KiCad design blocks library for FineFab. Contains reusable design blocks across 8 categories, project templates, custom KiCad symbols, and SPICE simulation files.

## Commands

```bash
# KiCad CLI — export schematic to PDF
kicad-cli sch export pdf <project>.kicad_sch -o output/

# KiCad CLI — run ERC
kicad-cli sch erc <project>.kicad_sch

# KiCad CLI — export netlist for spice-life
kicad-cli sch export netlist <project>.kicad_sch -o ../spice-life/circuits/

# Validate a design block (ERC + DRC)
kicad-cli sch erc blocks/<block>/schematic.kicad_sch
kicad-cli pcb drc blocks/<block>/board.kicad_pcb

# Run SPICE simulation (ngspice)
ngspice -b <file>.cir
```

## EDA MCP Pipeline

Complete schéma-to-JLCPCB pipeline available via MCP tools:

| Step | MCP Server | Use |
|------|-----------|-----|
| Sourcing | `jlcmcp-remote` | Quick stock/pricing lookup (1.5M+ parts, zero config) |
| Sourcing | `jlcpcb-search` | Offline SQLite search (450k+ parts, datasheets, price tiers) |
| Schematic | `kicad-sch` | Symbol placement, wires, ERC |
| PCB Layout | `kicad-pcb`, `kicad-design` | Placement, design rules, manual routing |
| Autoroute | `kicad-design` | Freerouting Docker, DRC post-route |
| Review | kicad-happy skills | DFM, EMC 42 rules, thermal, tolerance |
| Export | `kicad-design` | Gerbers, BOM with LCSC IDs, CPL with rotations, STEP 3D |
| Fabrication | `kicad-fab` | Async autoroute, organized output dirs |

## JLCPCB Part Selection Strategy

- **Basic parts** (`library_type="no_fee"`): zero assembly fee — prefer these
- **Preferred parts**: small fee — acceptable for specialized components
- **Extended parts**: +$3/unique part — avoid unless no alternative
- kicad-happy `jlcpcb` skill handles rotation offset table automatically

## MCP & outils disponibles (alternatifs)

| Outil | Commande / MCP | Usage |
|-------|----------------|-------|
| KiCad MCP (Kill_LIFE) | `.mcp.json` racine | Schéma, PCB, DRC/ERC headless |
| KiCad MCP (Seeed-Studio) | MCP GrosMac | 39 outils, pin analysis, device tree |
| KiCad MCP (mixelpixx) | MCP GrosMac | 122 outils, JLCPCB, routage avancé |
| SPICEBridge | MCP GrosMac | Simulation analogique ngspice, 18 outils |
| ngspice MCP (Kill_LIFE) | `.mcp.json` racine | Simulation SPICE directe |
| Context7 | MCP oh-my-claude | Docs KiCad/composants live |

Skill : `eda-kicad` (dans `../skills/eda-kicad/`).

## Architecture

```
*.kicad_pro     — KiCad project
*.kicad_sch     — schematics
*.kicad_pcb     — PCB layout
*.cir / *.sp    — SPICE netlists
fab/            — Gerber/drill output for manufacturing
blocks/         — reusable design blocks (8 categories)
```

## Pipeline hardware

```text
KiCad schéma  →  ERC  →  SPICEBridge simulation  →  PCB layout  →  DRC  →  Gerbers
     ↓                         ↓                                         ↓
 netlist export         vérification specs                        BOM JLCPCB
 → spice-life/          (filtres, alims)                          → fab/
```

## Anti-Patterns / Notes

- Schematic changes must propagate to spice-life: re-export netlist then re-run `pytest tests/` in spice-life
- Fab outputs (Gerbers) are generated artifacts — regenerate, don't hand-edit
- Pin assignments must match makelife-firmware constants
- Never commit binary KiCad autosave files (`*-bak`, `*-rescue`)
- Use KiCad 8+ CLI for automated exports in CI
- Toujours 100nF céramique par pin VCC IC, placé < 3mm
- Pull-ups sur I2C, SPI CS, reset — vérifier avant layout
- ESD protection sur connecteurs externes (USB, antenne)
- Vérifier dispo JLCPCB (basic vs extended) avant choix composant
