r_body = 0.04480242 # m
m_body = 38 # g

r_nuts = [ # m
    0.10561734,
    0.11535387,
    0.12583194,
    0.13398521
] * 2
m_8_nuts = 28 # g
m_single_nut = m_8_nuts/8

m_total = m_body + m_8_nuts

# calculate overall CoM (r_total) by [(r_body*m_body) + (r_1*m_1) + ... + (r_8*m_8)] / m_total
# equivalent to [(r_body*m_body) + (r_sum_nuts*m_sum_nuts)] / m_total

r_total = ((r_body * m_body) + (sum(r_nuts) * m_single_nut))
r_total_avg = ((r_body * m_body) + (sum(r_nuts) * m_single_nut)) / m_total

g = 9.81 # m/s/s