import py_dss_interface
from py_dss_toolkit import dss_tools

dss = py_dss_interface.DSS()

dss_file = r"C:\Dados_teste\OpenDSS\CBA\Alim_Meia_Ponte_5_REDUZIDO\Master_PyDSS_Interface.dss"

dss_tools.update_dss(dss)

dss.text(f"compile [{dss_file}]")

dss.text(f"buscoords BusCoords.csv")

dss.text("set mode=daily")
dss.text("set stepsize=1h")
dss.text("set number=1")

for h in range(24):
    if dss.solution.hour == 24:
        dss.meters.reset_all()
    dss.solution.solve()

#dss.text("sample")

meter_values = dss.meters.register_values

print(f"Energia total: {meter_values[0]:.2f} kWh")
print(f"Perdas totais: {meter_values[12]:.2f} kWh")

monitor_name = "feeder"
monitor = dss_tools.results.monitor(monitor_name)
monitor["Total Power"] = monitor[' P1 (kW)'] + monitor[' P2 (kW)'] + monitor[' P3 (kW)']
dss_tools.static_view.p_vs_time(monitor_name, show=True)

