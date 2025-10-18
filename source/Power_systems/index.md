---
hide:
  - navigation
  - toc
---

<section style="padding:1rem 1rem; text-align:center; background:#f9fafb;">
  <h1 style="font-size:1rem; margin-bottom:1rem;">Power System Notes</h1>
  <p style="max-width:720px; margin:0 auto; font-size:0.7rem; color:#444;">
    Documentation on foundational and advanced modeling techniques in power systems — including phasor-domain and EMT-domain analysis with applications in grid stability, renewables, and converter behavior.
  </p>
</section>

<div style="justify-content:center; overflow-x:auto; padding:1rem;">
  <h1 style="text-align:center; font-size:1rem; margin-bottom:1rem;">Power System Classification</h1>

```mermaid
%%{init: {"theme": "base", "themeVariables": {
  "primaryColor": "#000000ff",
  "primaryTextColor": "#fff",
  "fontSize": "14px",
  "fontFamily": "Inter, sans-serif"
  },
  "flowchart": {
    "curve": "linear"
  }
  }}%%

flowchart TD
    %% Root
    A["Power System Stability"]:::root

    %% Level 1
    A --> B["Angle Stability"]
    A --> C["Frequency Stability"]
    A --> D["Voltage Stability"]

    %% Rotor Angle Stability Branch
    B --> B1["Small-Signal<br>Stability"]
    B --> B2["Transient Stability"]
    B1 --> B3["Non-Oscillatory<br>Instability"]
    B2 --> B4["Oscillatory<br>Instability"]

    %% Frequency Stability Branch
    C --> C1["Mid-term<br>Stability"]
    C --> C2["Long-term<br>Stability"]

    %% Voltage Stability Branch
    D --> D1["Large-Disturbance<br>Voltage Stability"]
    D --> D2["Small-Disturbance<br>Voltage Stability"]

    %% Clickable Links
    click A "/stability/overview" "Overview of Power System Stability"
    click B "/stability/rotor-angle" "Rotor Angle Stability"
    click B1 "/stability/small-disturbance-angle" "Small Disturbance Angle Stability"
    click B2 "/stability/transient" "Transient Stability"
    click C "/stability/frequency" "Frequency Stability"
    click D "/stability/voltage" "Voltage Stability"
    click D1 "/stability/large-disturbance-voltage" "Large Disturbance Voltage Stability"
    click D2 "/stability/small-disturbance-voltage" "Small Disturbance Voltage Stability"

    %% Styling
    classDef root fill:#2563eb,color:#fff,stroke:none,font-weight:bold;
    classDef default fill:#fff,stroke:#2563eb,stroke-width:1px,color:#111;
```
<p style="text-align:center; justify-content:center; font-size:0.7rem; color:#666; font-style:italic; margin-top:0.5rem;">
  Reference: Power System Stability and Control - Second Edition
</p>
</div>