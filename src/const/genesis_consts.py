from enum import Enum

class TerraParametros(Enum):
    R_ref = 1.0
    M_ref = 1.0
    F_ref = 1.0
    T_ref = 255.0
    g_ref = 1.0
    sigma_r = 0.3
    sigma_m = 0.5
    sigma_f = 0.3
    sigma_t = 30.0
    sigma_g = 0.25

class DatasetColumns(Enum):
    pl_name = "pl_name"
    hostname = "hostname"
    sy_snum = "sy_snum"
    sy_pnum = "sy_pnum"
    pl_orbper = "pl_orbper"
    pl_rade = "pl_rade"
    pl_bmasse = "pl_bmasse"
    pl_insol = "pl_insol"
    pl_eqt = "pl_eqt"
    sy_dist = "sy_dist"
    st_logg = "st_logg"