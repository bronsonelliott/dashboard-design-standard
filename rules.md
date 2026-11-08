# Rule reference

Every rule in the Dashboard Design Standard (version 1.0.0), by section, plus the color palette. The full standard, with the reasoning and every example, is [index.html](index.html). This page is generated from it by `make_rules.py`, so the two always match.

## Rule levels

- **MUST**: release gate. Fix any failure before shipping, or record why the rule does not apply.
- **SHOULD**: expected practice. Record a reason, tradeoff and mitigation for each departure. The reviewer agrees before release.
- **GUIDANCE**: a suggested technique.

**How levels are assigned.** MUST when breaking it can mislead a reader, hide a signal the decision needs, block access, or skip a release control. SHOULD when it is a strong default with legitimate exceptions, or a MUST rule elsewhere already enforces its core. GUIDANCE for judgment calls. Use the same test for any new rule.

**Counts:** 64 rules — 38 MUST, 24 SHOULD, 2 GUIDANCE.

## All rules


### 01 Purpose and scope

| ID | Level | Rule |
|---|---|---|
| PUR-01 | MUST | Name the audience, recurring decision and action. Keep a first-screen item only when the brief identifies the decision it supports. |
| PUR-02 | SHOULD | Move exhaustive records, open-ended exploration and multi-step workflows to the appropriate companion surface. Link from the relevant summary. |
| PUR-03 | GUIDANCE | Start a requirements meeting with a recent decision. Ask what evidence made someone act, and sketch only the information they used. |

### 03 Choose the dashboard type

| ID | Level | Rule |
|---|---|---|
| TYP-01 | MUST | Record one primary type, decision deadline and default audience in the brief. Design the overview around that combination. |

### 04 Gather requirements

| ID | Level | Rule |
|---|---|---|
| REQ-01 | MUST | Get the business owner’s agreement on a one-page brief before building the production view. Record the agreed device and viewport, default scope and test scenarios. |
| REQ-02 | MUST | Assign a measure owner and approved source for every headline measure. Record the calculation, inclusion rules, unit, grain, comparator, target direction, period boundaries, refresh and maximum data age. |
| REQ-03 | SHOULD | Agree a measurable acceptance test with typical readers. Time an uncoached read of the default view, then test a threshold case, missing data and the path to action. |

### 05 Measures and context

| ID | Level | Rule |
|---|---|---|
| MEA-01 | MUST | Label every displayed measure with its unit and time scope. Give decision measures a named comparison or explicitly state that no valid comparator exists and why. |
| MEA-02 | MUST | Match the comparator on definition, population, time grain and elapsed period. Label deliberate differences, such as comparing a partial actual with a future target, and show pace or a labeled projection where the decision depends on being on track. |
| MEA-03 | MUST | Compute rates from their underlying numerator and denominator at the displayed grain. Apply status and thresholds to full precision. Distinguish actual zero, missing, insufficient, partial and stale values. |
| MEA-04 | MUST | When assigning a rating, define the direction of improvement, inclusive and exclusive cutoffs, owner and action. Use words with a distinct mark and give unknown or stale its own state. |
| MEA-05 | SHOULD | Pair summaries with the exception, spread or segment that can change the decision. For a short ranked list, state the sort, count shown and total or link to the full list. |

### 06 Choose a visualization

| ID | Level | Rule |
|---|---|---|
| VIS-01 | MUST | Use a labeled scale that preserves the encoded relationship. Every length bar starts at zero, including each signed bar at the visible zero line. A line or dot may use a labeled focused scale if it preserves the intended comparison. |
| VIS-02 | MUST | For panels intended to compare magnitudes, align units, time windows, category order and scale domains. If the task compares shapes on independent scales, label each scale and the purpose. |
| VIS-03 | MUST | Show missing observations as gaps or explicit states. Distinguish forecasts from actuals with a named boundary and a different line style or mark. Use verified intervals when uncertainty could change the decision. |
| VIS-04 | GUIDANCE | Choose the simplest display that answers the question. Use aligned position or length before area, and separate series into panels when a combined view obstructs comparison. |
| DSP-01 | SHOULD | Pair the value with a name, unit, period and decision context. |
| DSP-02 | MUST | Use a common linear scale, a prominent featured mark and a short perpendicular comparison marker. A length bar starts at zero. Use a point for a focused scale. Include bands only for approved cutoffs and state their direction in text. |
| DSP-03 | SHOULD | Place the sparkline beside its current value. State the time window and grain, mark the latest point and share scales where magnitudes are compared. |
| DSP-04 | MUST | Start the value axis at zero. Keep lengths comparable and sort by value unless a meaningful category order should take precedence. |
| DSP-05 | MUST | Use equally spaced positions for regular reporting buckets and elapsed-time positions for irregular observations. Show the first and last periods, units and a labeled scale. Leave gaps where data is missing. |
| DSP-06 | MUST | Use one labeled scale and compatible units and time grain. Start bars at zero. Distinguish the benchmark line by style and label. |
| DSP-07 | MUST | Stack mutually exclusive parts on a common zero origin. Keep segment order stable. State the denominator for 100% stacks and directly identify the parts. |
| DSP-08 | SHOULD | Use one row per category and a labeled numeric axis. Show exact values when a focused domain is needed. |
| DSP-09 | MUST | Use contiguous equal-width numeric bins and a zero count baseline. State the bin width and observation count. State how boundary values are assigned. |
| DSP-10 | SHOULD | State the box, whisker and outlier definitions. Give each group’s sample size and use a shared scale. |
| DSP-11 | SHOULD | Name both axes with units and name the observation grain. Show overlap with an explicit method when it obscures the pattern. |
| DSP-12 | SHOULD | Repeat the same chart structure, encoding, date range and ordering across panels. Apply VIS-02 to every scale. |
| DSP-13 | SHOULD | Use explicit headers and units, a known sort order and right-aligned numbers. Add an adjacent visual only when it supports a distinct task. |
| DSP-14 | SHOULD | Size each rectangle by its share of the parent. Label hierarchy, units and values. Use boundaries and provide a readable ranked table or list. |
| DSP-15 | SHOULD | Use one visible zero reference. Show sign and units directly and name the baseline. |
| DSP-16 | SHOULD | Use verified spatial coordinates, show orientation or scale where relevant, and state the decision supported by location. Include a text equivalent. |

### 07 Displays to avoid or restrict

| ID | Level | Rule |
|---|---|---|
| AVD-01 | MUST | Keep monitoring charts two-dimensional. Exclude pies, donuts, radial gauges, radar charts and dual-scale charts from the monitoring view. Use the replacements below. |
| AVD-02 | MUST | Use a map only when a spatial relationship changes the decision. Plot trustworthy positions on appropriate geometry and make values available as text. |

### 08 Layout and arrangement

| ID | Level | Rule |
|---|---|---|
| LAY-01 | MUST | At the agreed desktop viewport or primary monitoring display, show all essential signals, exceptions and scope in one view at default zoom without scrolling or switching tabs. At narrow widths or zoom, follow ACC-03. |
| LAY-02 | SHOULD | Align components to a shared grid. Use a smaller gap within a group than between groups. Use whitespace and headings first, adding borders only where alignment or grouping needs them. |
| LAY-03 | MUST | Place the highest-priority signal or exception before its supporting detail in visual and reading order. Keep a headline measure, its comparison and its status in the same region. |
| LAY-04 | SHOULD | Put shared scope controls next to the heading and local controls inside their group. Preserve labels and reading order when the layout reflows. |
| LAY-05 | SHOULD | Keep detail pages out of the critical overview path. Name the destination, preserve applicable scope on entry, and provide a predictable return to the same overview state. |
| LAY-06 | SHOULD | Show no more than nine data items on the primary view. Count a small-multiples set or a sparkline table as one item. |

### 09 Color standards

| ID | Level | Rule |
|---|---|---|
| COL-01 | MUST | Use muted marks by default and one focal highlight hue per view. Give each color one meaning within a dashboard, including across filters, linked detail and refreshes. Keep status colors reserved for statuses. |
| COL-02 | MUST | Pair status with readable words and a distinct shape. Pair categorical or signed color with labels, line style, marker shape or aligned position. Check grayscale and common color-vision simulations. |
| COL-03 | MUST | Meet 4.5:1 for normal text and 3:1 for large text, essential graphical boundaries and required control states against adjacent colors. For this test, large text is at least 18 pt regular or 14 pt bold, approximately 24 or 18.7 CSS px respectively. Test actual pairs after blending. Use the permitted palette pairings below. |
| COL-04 | SHOULD | Use a sequential scale for increasing magnitude and a diverging scale only around a meaningful midpoint. Label units and class boundaries, including the midpoint and missing state. Give the same value the same color across comparable views. |
| COL-05 | MUST | Check the dashboard against each forbidden use below. Remove any occurrence from production views. |

### 10 Typography and number formatting

| ID | Level | Rule |
|---|---|---|
| TYPF-01 | SHOULD | Use one readable sans-serif family. At the design viewport, start at 24–32 CSS px for the page title, 24–36 for primary values, 16–20 for section titles, 14–16 for data and controls, and 12–14 for secondary notes and ticks. Resolve crowding by removing redundant content. |
| TYPF-02 | SHOULD | Right-align numeric table cells within a column and use tabular digits where supported. Keep the same units, precision and sign convention within a comparable series or column. |
| TYPF-03 | MUST | Display units and time labels without ambiguity. Use the dashboard’s declared locale and currency. Apply display rounding only after calculation and preserve exact source precision in authorized detail when the decision requires it. |

### 11 Text, titles and labels

| ID | Level | Rule |
|---|---|---|
| TXT-01 | SHOULD | Title each chart with its monitoring question or a supported current finding. If the title states a finding, update it when filters, refresh or missing data invalidate it. |
| TXT-02 | MUST | Name every axis, series and marker that would otherwise be ambiguous. Prefer direct labels when legible. If needed, place a compact legend beside the plot with matching order and non-color cues. |
| TXT-03 | MUST | Show current scope, latest successful data-as-of time and stale or partial state where the reader makes the decision. Put full definitions, sources and cutoff notes in a labeled footnote or linked definition. |
| TXT-04 | SHOULD | Use the business’s own terms in plain language. Define each acronym at first use on the dashboard or in its linked definitions. |

### 12 Interaction

| ID | Level | Rule |
|---|---|---|
| INT-01 | MUST | Make the default view answer the primary monitoring question without interaction. Show active filters, affected scope and a reset path when filters are available. |
| INT-02 | MUST | Make drill paths deliberate. Pass the selected entity and relevant scope, show the context at the destination, and keep required information available without hovering. |
| INT-03 | SHOULD | Reserve tooltips for extra precision or supporting context. Where present, make the same content reachable by keyboard and touch or via an equivalent visible route. |
| INT-04 | MUST | For every automated alert, define trigger, duration or repeat rule, recipient, action, resolution and stale-data behavior. Test that refresh does not cause repeated notifications for the same unresolved event. |

### 13 Accessibility

| ID | Level | Rule |
|---|---|---|
| ACC-01 | MUST | Operate every control with a keyboard. Use a logical focus order, visible and unobscured focus, and a way to leave each control. Preserve focus during refresh and return it predictably after dismissing a panel. |
| ACC-02 | MUST | Give each chart a meaningful accessible name and provide an equivalent readable summary or data table. Expose control names, values, states and table headers. Announce meaningful changes without reading every refresh. |
| ACC-03 | MUST | Keep text and controls usable at 200% text resize. At 320 CSS px width or equivalent 400% zoom, reflow content in reading order without page-level horizontal scrolling. Where a chart or data table genuinely requires two dimensions, contain its scrolling and provide an equivalent readable alternative. |
| ACC-04 | MUST | Verify contrast and non-color cues, complete the core tasks by keyboard, and read the overview, changed filters and detail using a supported screen reader. If the chart surface cannot provide equivalent access, include an accessible route before release. |
| ACC-05 | MUST | Make hover or focus disclosures dismissible, hoverable and persistent where WCAG 1.4.13 applies. Provide a visible or equivalent touch path for the same information. |

### 14 Review and governance

| ID | Level | Rule |
|---|---|---|
| GOV-01 | MUST | Before release, have the dashboard owner validate the decisions and measures, and a BI peer verify the checklist against the actual delivery surface. Close all MUST findings and record evidence for every pass or inapplicable rule. |
| GOV-02 | MUST | Record each SHOULD departure with its rule ID, affected audience, evidence, risk, mitigation, approver and expiry or review date. MUST failures block release. Fix the failure or use an approved delivery surface that passes. |
| GOV-03 | SHOULD | Re-review when audience, scope, measure definitions, targets, refresh, major layout or interactions change. Record the dashboard version and the standard version reviewed. |

## Palette (light)

| Role | Hex | Approved use and contrast |
|---|---|---|
| Canvas | `#FFFFFF` | Default reading and plot surface. |
| Subtle surface | `#F2F5F7` | Quiet group or table header fill. |
| Primary text | `#17242C` | Titles, key values, essential dark outlines. Text on canvas 15.85:1, on subtle 14.47:1. |
| Secondary text | `#344955` | Labels, supporting prose and notes. Text on canvas 9.42:1, on subtle 8.60:1. |
| Muted text | `#526370` | Metadata and Unknown status. Text on canvas 6.22:1, on subtle 5.68:1. |
| Gridlines | `#D7E0E5` | Decorative guides and row dividers only. |
| Axis and boundary | `#647581` | Essential axes or control outlines on canvas and subtle surfaces. 4.77:1 on canvas, 4.36:1 on subtle. Use the text tiers for tick labels. |
| Series 1 | `#4F6978` | Default bars, lines and points. White text on fill 5.79:1. Mark on canvas 5.79:1, on subtle 5.29:1. |
| Series 2 | `#705F7B` | Second category when it has a labeled role. White text on fill 5.81:1. Mark on canvas 5.81:1, on subtle 5.31:1. |
| Series 3 | `#726541` | Third category when it has a labeled role. White text on fill 5.75:1. Mark on canvas 5.75:1, on subtle 5.25:1. |
| Highlight | `#005DA6` | Focus, links and one focal chart role. Text on canvas 6.74:1, on subtle 6.15:1. |
| Within limit | `#21604E` | Status only. Use a circle and words. Text on canvas 7.37:1, on subtle 6.73:1. |
| Watch | `#765210` | Status only. Use a diamond and words. Text on canvas 7.04:1, on subtle 6.43:1. |
| Act | `#963528` | Status only. Use a triangle and words. Text on canvas 7.40:1, on subtle 6.76:1. |
| Bullet · Act | `#C6D0D8` | Darkest neutral background band. Ink featured bar has 10.12:1 contrast. Ink text on fill 10.12:1. |
| Bullet · Watch | `#DFE6EB` | Middle neutral background band. Ink featured bar has 12.57:1 contrast. Ink text on fill 12.57:1. |
| Bullet · Within limit | `#F0F3F5` | Lightest neutral band. Ink featured bar has 14.22:1 contrast. Ink text on fill 14.22:1. |
| Sequential · 1 low | `#D8E7F2` | Lightest magnitude class. Ink text on fill 12.55:1. |
| Sequential · 2 | `#91B6D1` | Second magnitude class. Ink text on fill 7.41:1. |
| Sequential · 3 | `#426C91` | Third magnitude class. White text on fill 5.55:1. |
| Sequential · 4 high | `#245578` | Darkest magnitude class. White text on fill 7.94:1. |
| Diverging · far below | `#913E2D` | Strong negative deviation. White text on fill 7.17:1. |
| Diverging · below | `#DEAA99` | Moderate negative deviation. Ink text on fill 7.78:1. |
| Diverging · midpoint | `#F0F3F5` | Neutral midpoint. Label its numeric meaning. Ink text on fill 14.22:1. |
| Diverging · above | `#9ABEBB` | Moderate positive deviation. Ink text on fill 7.89:1. |
| Diverging · far above | `#21605E` | Strong positive deviation. White text on fill 7.24:1. |
