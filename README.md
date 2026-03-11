![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# O2O

## Architecture Overview

```
O2OData (entry point)
  ├── ChargeDataSet        → Load .mzML file (via pyopenms)
  ├── JoinSpectra          → Extract doublet pairs across all spectra
  │     └── NeoPower       → Find peak pairs with Δm ≈ 2.004 Da within a single spectrum
  ├── O2Omachine           → Core analysis pipeline
  │     ├── AdjacencyMatGen    → Build adjacency matrix (RT + m/z proximity)
  │     │     ├── RT_Diference
  │     │     └── mz_Diference
  │     ├── Centroids          → Identify seed clusters via max intensity
  │     │     └── MaxIntCentroids
  │     │           └── ModulesDetMax  → Recursive neighbor expansion
  │     ├── RawKernel          → Compute cluster statistics for kernels
  │     │     └── Signals_Stats
  │     ├── ModulesK_Nearst    → Assign all signals to nearest kernel
  │     │     ├── DistanceKernel
  │     │     ├── Pre_SelectCentroid
  │     │     └── SelectCentroid
  │     ├── SummaryClusters    → Statistical summary per cluster
  │     │     ├── Cluster_Stats
  │     │     │     ├── Signals_Stats
  │     │     │     └── WelchTest
  │     │     └── → Output DataFrame
  │     └── ShowDF             → Display results
  └── gc.collect() everywhere
```

---
