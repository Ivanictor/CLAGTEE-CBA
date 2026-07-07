import py_dss_interface
from py_dss_toolkit import dss_tools
import pandas as pd

dss = py_dss_interface.DSS()

dss_file = r"C:\Dados_teste\OpenDSS\OpenDSS 23-06-2026\Run Rede1 Monitors.dss"

dss_tools.update_dss(dss)

dss.text(f"compile [{dss_file}]")

dss.text("set mode=daily")
dss.text("set stepsize=1h")
dss.text("set number=48")

dss.solution.solve()

meter_values = dss.meters.register_values

print(f"Energia total: {meter_values[0]:.2f} kWh")
print(f"Perdas totais: {meter_values[12]:.2f} kWh")