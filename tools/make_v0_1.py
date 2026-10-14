"""Update parameters_v0.json in place (2026-10-14): state the charge-reference occupations explicitly and set the screening factors re-determined on
the final operators. No separate version file and no changelog (PI instruction: a superseded parameter set must not stay in the repository).
usage: python3 tools/make_v0_1.py <s_Vsp> <s_Vd> <s_O> <eta>"""
import json, sys, re
sVsp, sVd, sO, eta = (float(x) for x in sys.argv[1:5])
d = json.load(open("parameters_v0.json"))
cr = d["charge_response"]
cr["mapping"] = "charge-conserving, Coulomb metric; reference-atom occupations on the first radial of each shell (see reference_occupations); added d radials carry no reference charge"
cr["reference_occupations"] = {"V": {"4s": 1.0, "4p": 0.0, "3d": 4.0, "dR_3d/dn_3d": 0.0, "d2R_3d/dn_3d^2": 0.0}, "O": {"2s": 2.0, "2p": 4.0},
                                "note": "the same 3d4 4s1 / 2s2 2p4 configurations as the reference atoms of the reference Hamiltonian"}
cr["screening"] = {"s_Vsp": sVsp, "s_Vd": sVd, "s_O": sO}; cr["eta"] = eta
cr["determination"] = "joint fit to the 22 matched PBE linear responses of VO2-R (14) and V2O3 (8) on the final operators, M1 held out; eta = 0 is the optimum (the fit quality degrades monotonically for eta > 0 up to 0.05 bohr^-2)"
d.pop("changelog", None)
json.dump(d, open("parameters_v0.json", "w"), indent=2, ensure_ascii=False); open("parameters_v0.json", "a").write("\n")
r = open("README.md").read()
r = r.replace("- reference atoms (neutral, unconfined, all-electron PBE; V 3d⁴4s¹, O 2s²2p⁴) and frozen cores (V 1s–3p, O 1s);",
              "- reference atoms (neutral, unconfined, all-electron PBE; V 3d⁴4s¹, O 2s²2p⁴) and frozen cores (V 1s–3p, O 1s); the charge reference of the response carries the same occupations on the first radial of each shell;")
r = re.sub(r"- the charge-response screening factors θ⁽⁰⁾ = \(s_Vsp, s_Vd, s_O, η\) = \([^)]*\);",
           f"- the charge-response screening factors θ⁽⁰⁾ = (s_Vsp, s_Vd, s_O, η) = ({sVsp}, {sVd}, {sO}, {eta:g});", r)
open("README.md", "w").write(r)
print("parameters_v0.json and README.md updated in place; θ =", (sVsp, sVd, sO, eta))
