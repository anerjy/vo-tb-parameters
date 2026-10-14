# V–O tight-binding model: v0 parameters

Parameters of the v0 tight-binding model for vanadium oxides described in the manuscript

> Jun-qiang Lu, *A Parameter-Free Reference Hamiltonian for Tight-Binding Vanadium Oxides*,
> [arXiv:2610.17687](https://arxiv.org/abs/2610.17687) (2026).

`parameters_v0.json` gives the parameters and numerical settings of the model and the rules that fix its atomic functions (lengths in bohr):

- reference atoms (neutral, unconfined, all-electron PBE; V 3d⁴4s¹, O 2s²2p⁴) and frozen cores (V 1s–3p, O 1s);
- the 3ζ-d basis: confinement radii and radial set;
- the declared atomic-function tails, supports and matching rule;
- the reference-operator and C₀ quadrature settings;
- the charge-response screening factors θ⁽⁰⁾ = (s_Vsp, s_Vd, s_O, η) = (0.439, 0.797, 0.913, 0);
- occupation smearing conventions.

The reference Hamiltonian has no adjustable terms; the three screening factors are the only quantities determined from
data (PBE linear responses of VO₂-R and V₂O₃). See the paper for definitions and validation.
