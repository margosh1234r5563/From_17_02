rain_level_cm = 1
square_rain_g = 1
square_rain_gm_2 = square_rain_g * (10 ** 6)
rain_level_dm = rain_level_cm / 10
v_rain = square_rain_gm_2 * rain_level_dm
print(v_rain)
