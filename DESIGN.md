---
version: alpha
name: Model Passports
description: Machined identity plates for the rapidly changing model ecosystem.
colors:
  primary: "#080A0D"
  secondary: "#151922"
  tertiary: "#B8FF3D"
  neutral: "#F4F7FB"
  muted: "#8B95A7"
  cyan: "#6DE1FF"
  violet: "#A98BFF"
  amber: "#FFCB66"
  danger: "#FF6F7D"
typography:
  display:
    fontFamily: Geist
    fontSize: 1.125rem
    fontWeight: 650
    lineHeight: 1.05
    letterSpacing: "-0.02em"
  label:
    fontFamily: JetBrains Mono
    fontSize: 0.625rem
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0.14em"
rounded:
  sm: 3px
  md: 8px
  lg: 14px
spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
components:
  passport-shell:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.lg}"
    padding: 12px
  variant-band:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.sm}"
    padding: 4px
  capability-pip:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.cyan}"
    rounded: "{rounded.sm}"
    padding: 4px
  metadata-label:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: 4px
  reasoning-pip:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.violet}"
    rounded: "{rounded.sm}"
    padding: 4px
  preview-state:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.amber}"
    rounded: "{rounded.sm}"
    padding: 4px
  deprecated-state:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.danger}"
    rounded: "{rounded.sm}"
    padding: 4px
---

## Overview

Model Passports are compact identity instruments, not decorative stickers. The visual language combines an aerospace data plate, a minted security credential, and restrained heraldry. Every mark communicates one atomic fact.

A full Passport is data. A Sigil is a rendering of that data. A serving route is an overlay, never the model's identity.

## Colors

The foundation is graphite rather than pure black. Text is cold white. One electric signal color marks verified identity; cyan marks capability, violet reasoning, amber lifecycle warnings, and red unavailable or deprecated state.

Provider colors may appear only inside the maker chamber. They must not recolor the badge or become capability semantics.

## Typography

Model names use a compact geometric grotesk. Metadata uses a monospaced face with uppercase labels and tabular numbers. Text fallbacks preserve complete model and route names.

## Layout

The canonical wide sigil has five zones:

1. **Maker chamber** — company logo or deterministic monogram.
2. **Identity field** — family, generation, and exact display name.
3. **Variant band** — provider-authored tier such as Sonnet, Flash, or Mini.
4. **Capability rail** — at most five prioritized pips; overflow moves to details.
5. **Route tab** — serving provider, visually subordinate and detachable.

Compact and terminal forms collapse zones without changing their semantic order.

## Elevation & Depth

Use a double bezel: a dim structural outer rail and slightly raised inner plate. Highlights are optical edges, not generic shadows. Motion is limited to state transitions and active-route scans; static identity never pulses.

## Shapes

Lifecycle changes the outer ring: stable is continuous; preview is segmented; deprecated is broken; local doubles the lower edge; open weights creates an opening in the upper-right arc.

## Components

### Maker mark

Use a reviewed company logo when redistribution and trademark use are acceptable. Otherwise generate a deterministic two-letter monogram.

### Variant band

Preserve vendor language verbatim. Never map Opus to Sol, Sonnet to Terra, or Haiku to Luna as fact. Cross-provider positioning must declare source and confidence separately.

### Capability pips

Atomic vocabulary: `R` reasoning, `V` vision, `T` tools, `S` structured output, `A` audio, `I` image, `O` open weights, `L` local. Every pip has a full accessible label. Absence means unknown unless a source explicitly states false.

### Route tab

Format: `VIA <PROVIDER>`. It may encode direct, brokered, local, free, subscription, or preview state, but may not replace the maker mark.

## Do's and Don'ts

- Do separate canonical model identity from serving route.
- Do preserve source, timestamp, and confidence for mutable facts.
- Do render unknown honestly and provide SVG, text, and accessible-name equivalents.
- Don't hotlink logos, imply endorsement, or use badges for authorization/routing gates.
- Don't create bespoke illustrations for thousands of model IDs.
- Don't encode meaning through color alone.
