# makelife-hard

KiCad hardware design and SPICE simulation files for FineFab electronics.

## Commands

```bash
# KiCad CLI — export schematic to PDF
kicad-cli sch export pdf <project>.kicad_sch -o output/

# KiCad CLI — run ERC
kicad-cli sch erc <project>.kicad_sch

# KiCad CLI — export netlist for spice-life
kicad-cli sch export netlist <project>.kicad_sch -o ../spice-life/circuits/

# Run SPICE simulation (ngspice)
ngspice -b <file>.cir
```

## Architecture

```
*.kicad_pro     — KiCad project
*.kicad_sch     — schematics
*.kicad_pcb     — PCB layout
*.cir / *.sp    — SPICE netlists
fab/            — Gerber/drill output for manufacturing
```

## MCP & outils disponibles

| Outil | Commande / MCP | Usage |
|-------|----------------|-------|
| KiCad MCP (Kill_LIFE) | `.mcp.json` racine | Schéma, PCB, DRC/ERC headless |
| KiCad MCP (Seeed-Studio) | MCP GrosMac | 39 outils, pin analysis, device tree |
| KiCad MCP (mixelpixx) | MCP GrosMac | 122 outils, JLCPCB, routage avancé |
| SPICEBridge | MCP GrosMac | Simulation analogique ngspice, 18 outils |
| ngspice MCP (Kill_LIFE) | `.mcp.json` racine | Simulation SPICE directe |
| Context7 | MCP oh-my-claude | Docs KiCad/composants live |

Skill : `eda-kicad` (dans `../skills/eda-kicad/`).

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
