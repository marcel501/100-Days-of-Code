#
# Mathematics Library "mathlib" Library
#

# Modules
from enum import Enum


# Available modes
class Modes(Enum):
    FORCE = 1
    STRESS = 2
    STRAIN = 3

# Units for modes
units = {
    Modes.FORCE: " N",
    Modes.STRESS: " N/m^2",
    Modes.STRAIN: ""
}

# Equations for modes
equations = {
    Modes.FORCE: "F = σ * A",
    Modes.STRESS: "σ = F / A",
    Modes.STRAIN: "ε = Δl / l"
}



