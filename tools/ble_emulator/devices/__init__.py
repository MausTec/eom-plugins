"""Registry of emulatable device profiles, keyed by CLI name."""

from . import lovense, lovense_edge, lovense_max, lovense_nora, nobra

PROFILES = {
    "lovense": lovense.PROFILE,
    "lovense-edge": lovense_edge.PROFILE,
    "lovense-max": lovense_max.PROFILE,
    "lovense-nora": lovense_nora.PROFILE,
    "nobra": nobra.PROFILE,
}
