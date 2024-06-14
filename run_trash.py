import aviary.api as av
from outputted_phase_info import phase_info
prob = av.run_aviary('models/test_aircraft/Ces-500.csv',
                     phase_info, optimizer="SLSQP", make_plots=True, max_iter=100)
print(prob.get_val(av.Mission.Summary.FUEL_BURNED, units='lbm')[0])